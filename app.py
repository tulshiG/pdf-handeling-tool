from flask import Flask, request, jsonify, send_file
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import os
import random
import math

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def apply_brightness(image_array, factor=1.2):
    return np.clip(image_array * factor, 0, 1)

def apply_grayscale(image_array):
    return np.dot(image_array[..., :3], [0.2989, 0.5870, 0.1140])[..., None].repeat(3, axis=2)

def apply_sepia(image_array):
    sepia_filter = np.array([[0.393, 0.769, 0.189],
                             [0.349, 0.686, 0.168],
                             [0.272, 0.534, 0.131]])
    return np.clip(image_array @ sepia_filter.T, 0, 1)

def apply_blur(image_array):
    kernel_size = 5
    kernel = np.ones((kernel_size, kernel_size)) / (kernel_size ** 2)
    return np.clip(np.apply_along_axis(
        lambda x: np.convolve(x, kernel.ravel(), mode='same'), axis=0, arr=image_array), 0, 1)

@app.route('/upload', methods=['POST'])
def upload_image():
    file = request.files['image']
    if file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        return jsonify({'message': 'Image uploaded successfully', 'path': file_path})
    return jsonify({'error': 'No image uploaded'}), 400

@app.route('/process', methods=['POST'])
def process_image():
    data = request.json
    image_path = data.get('image_path')
    filter_type = data.get('filter_type')

    if not os.path.exists(image_path):
        return jsonify({'error': 'Image not found'}), 404

    img = plt.imread(image_path)

    if filter_type == 'brightness':
        img = apply_brightness(img)
    elif filter_type == 'grayscale':
        img = apply_grayscale(img)
    elif filter_type == 'sepia':
        img = apply_sepia(img)
    elif filter_type == 'blur':
        img = apply_blur(img)

    output = BytesIO()
    plt.imsave(output, img, format='png')
    output.seek(0)
    return send_file(output, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
