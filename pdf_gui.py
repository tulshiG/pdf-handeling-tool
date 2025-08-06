import tkinter as tk
from tkinter import filedialog
from pdf import (  # Assuming your PDF functions are in 'pdf.py'
    merge_pdf,
    split_pdf,
    extract_text,
    extract_images,
    encrypt_pdf,
    decrypt_pdf,
    rearrange_pages,
    rotate_pages,
    read_metadata,
    add_metadata,
    optimise_pdf,
)


class PdfManipulationGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PDF Manipulation Tool")
        self.geometry("800x600")

        # Input File
        self.input_file_label = tk.Label(self, text="Input PDF File:")
        self.input_file_label.pack()
        self.input_file_entry = tk.Entry(self, width=50)
        self.input_file_entry.pack()
        self.input_file_browse_button = tk.Button(
            self, text="Browse", command=self.browse_input_file
        )
        self.input_file_browse_button.pack()

        # Output File
        self.output_file_label = tk.Label(self, text="Output PDF File:")
        self.output_file_label.pack()
        self.output_file_entry = tk.Entry(self, width=50)
        self.output_file_entry.pack()
        self.output_file_browse_button = tk.Button(
            self, text="Browse", command=self.browse_output_file
        )
        self.output_file_browse_button.pack()

        # Merge Button
        self.merge_button = tk.Button(self, text="Merge PDFs", command=self.merge_pdf)
        self.merge_button.pack()

        # Split Button
        self.split_button = tk.Button(self, text="Split PDF", command=self.split_pdf)
        self.split_button.pack()

        # Extract Text Button
        self.extract_text_button = tk.Button(
            self, text="Extract Text", command=self.extract_text
        )
        self.extract_text_button.pack()

        # Extract Images Button
        self.extract_images_button = tk.Button(
            self, text="Extract Images", command=self.extract_images
        )
        self.extract_images_button.pack()

        # Additional Function Buttons (add as needed)
        self.encrypt_button = tk.Button(self, text="Encrypt PDF", command=self.encrypt_pdf)
        self.encrypt_button.pack()
        self.decrypt_button = tk.Button(self, text="Decrypt PDF", command=self.decrypt_pdf)
        self.decrypt_button.pack()
        # ... Add buttons for other functionalities

        # Entry for Additional Parameters (if needed)
        self.password_entry = tk.Entry(self, width=20)  # For encrypt/decrypt
        self.password_entry.pack(show="*")  # Hide password characters
        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack()

        self.page_order_entry = tk.Entry(self, width=20)  # For rearrange_pages
        self.page_order_entry.pack()
        self.page_order_label = tk.Label(self, text="Page Order (comma-separated):")
        self.page_order_label.pack()

        self.rotation_entry = tk.Entry(self, width=20)  # For rotate_pages
        self.rotation_entry.pack()
        self.rotation_label = tk.Label(self, text="Rotation (degrees):")
        self.rotation_label.pack()

        self.title_entry = tk.Entry(self, width=20)  # For add_metadata
        self.title_entry.pack()
        self.title_label = tk.Label(self, text="Title:")
        self.title_label.pack()

        self.author_entry = tk.Entry(self, width=20)  # For add_metadata