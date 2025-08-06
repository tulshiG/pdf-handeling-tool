import numpy as np
import matplotlib.pyplot as plt
import random
import math

def load_image(file_path):
    """Load an image and return it as a numpy array."""
    image = plt.imread(file_path)
    return image / 255.0  # Normalize to 0-1 range

def save_image(image, file_path):
    """Save a numpy array as an image."""
    plt.imsave(file_path, np.clip(image, 0, 1))

def show_image(image, title="Image"):
    """Display an image using matplotlib."""
    plt.imshow(image, cmap="gray" if len(image.shape) == 2 else None)
    plt.title(title)
    plt.axis("off")
    plt.show()

def grayscale(image):
    """Convert an RGB image to grayscale."""
    return np.dot(image[..., :3], [0.299, 0.587, 0.114])

def adjust_brightness(image, factor):
    """Adjust brightness by multiplying pixel values by a factor."""
    return np.clip(image * factor, 0, 1)

def invert_colors(image):
    """Invert the colors of the image."""
    return 1 - image

def blur_image(image, kernel_size=3):
    """Apply a simple average blur."""
    h, w, c = image.shape
    blurred_image = np.zeros_like(image)
    pad = kernel_size // 2

    # Add padding to the image
    padded_image = np.pad(image, ((pad, pad), (pad, pad), (0, 0)), mode='constant', constant_values=0)

    # Convolve with the kernel
    for i in range(h):
        for j in range(w):
            for k in range(c):
                blurred_image[i, j, k] = np.mean(padded_image[i:i+kernel_size, j:j+kernel_size, k])

    return blurred_image

# Main script
if __name__ == "__main__":
    # Load the image
    image_path = "pic/image_2_1.jpeg"  # Replace with your image file path
    image = load_image(image_path)

    # Show original image
    show_image(image, title="Original Image")

    # Apply filters
    grayscale_img = grayscale(image)
    bright_img = adjust_brightness(image, factor=1.5)
    inverted_img = invert_colors(image)
    blurred_img = blur_image(image, kernel_size=5)

    # Display results
    show_image(grayscale_img, title="Grayscale Image")
    show_image(bright_img, title="Brightened Image")
    show_image(inverted_img, title="Inverted Colors")
    show_image(blurred_img, title="Blurred Image")

    # Save results
    save_image(grayscale_img, "grayscale_output.png")
    save_image(bright_img, "bright_output.png")
    save_image(inverted_img, "inverted_output.png")
    save_image(blurred_img, "blurred_output.png")
