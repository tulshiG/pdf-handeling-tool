import tkinter as tk
from tkinter import filedialog
from pdf import (
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
        self.input_file_label.grid(row=0, column=0, sticky="w") 
        self.input_file_entry = tk.Entry(self, width=50)
        self.input_file_entry.grid(row=0, column=1)
        self.input_file_browse_button = tk.Button(
            self, text="Browse", command=self.browse_input_file
        )
        self.input_file_browse_button.grid(row=0, column=2)

        # Output File
        self.output_file_label = tk.Label(self, text="Output PDF File:")
        self.output_file_label.grid(row=1, column=0, sticky="w")
        self.output_file_entry = tk.Entry(self, width=50)
        self.output_file_entry.grid(row=1, column=1)
        self.output_file_browse_button = tk.Button(
            self, text="Browse", command=self.browse_output_file
        )
        self.output_file_browse_button.grid(row=1, column=2)

        # Merge Button
        self.merge_button = tk.Button(self, text="Merge PDFs", command=self.merge_pdf)
        self.merge_button.grid(row=2, column=0, columnspan=3) 

        # Split Button
        #self.split_button = tk.Button(self, text="Split PDF", command=self.split_pdf)
        #self.split_button.grid(row=3, column=0, columnspan=3)

        # Extract Text Button
        self.extract_text_button = tk.Button(
           # self, text="Extract Text", command=self.extract_text
        )
        self.extract_text_button.grid(row=4, column=0, columnspan=3)

        # Extract Images Button
        self.extract_images_button = tk.Button(
            #self, text="Extract Images", command=self.extract_images
        )
        self.extract_images_button.grid(row=5, column=0, columnspan=3)

        # Encrypt Button
        #self.encrypt_button = tk.Button(self, text="Encrypt PDF", command=self.encrypt_pdf)
        #self.encrypt_button.grid(row=6, column=0, columnspan=3)

        # Decrypt Button
        #self.decrypt_button = tk.Button(self, text="Decrypt PDF", command=self.decrypt_pdf)
        #self.decrypt_button.grid(row=7, column=0, columnspan=3)

        # ... Add more buttons as needed

        # Entry for Additional Parameters (if needed)
        self.password_label = tk.Label(self, text="Password:")
        self.password_label.grid(row=8, column=0, sticky="w")
        self.password_entry = tk.Entry(self, width=20, show="*")
        self.password_entry.grid(row=8, column=1)

        self.page_order_label = tk.Label(self, text="Page Order (comma-separated):")
        self.page_order_label.grid(row=9, column=0, sticky="w")
        self.page_order_entry = tk.Entry(self, width=20)
        self.page_order_entry.grid(row=9, column=1)

        self.rotation_label = tk.Label(self, text="Rotation (degrees):")
        self.rotation_label.grid(row=10, column=0, sticky="w")
        self.rotation_entry = tk.Entry(self, width=20)
        self.rotation_entry.grid(row=10, column=1)

        self.title_label = tk.Label(self, text="Title:")
        self.title_label.grid(row=11, column=0, sticky="w")
        self.title_entry = tk.Entry(self, width=20)
        self.title_entry.grid(row=11, column=1)

        self.author_label = tk.Label(self, text="Author:")
        self.author_label.grid(row=12, column=0, sticky="w")
        self.author_entry = tk.Entry(self, width=20)
        self.author_entry.grid(row=12, column=1)

    def browse_input_file(self):
        filename = filedialog.askopenfilename(
            initialdir="/", title="Select Input PDF File", filetypes=[("PDF Files", "*.pdf")]
        )
        if filename:
            self.input_file_entry.delete(0, tk.END)
            self.input_file_entry.insert(0, filename)

    def browse_output_file(self):
        filename = filedialog.asksaveasfilename(
            defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")]
        )
        if filename:
            self.output_file_entry.delete(0, tk.END)
            self.output_file_entry.insert(0, filename)

    def merge_pdf(self):
        input_pdfs = self.input_file_entry.get().split(",")
        output_path = self.output_file_entry.get()
        merge_pdf(input_pdfs, output_path) 

    # ... (Implement other button click handlers similarly)

if __name__ == "__main__":
    gui = PdfManipulationGUI()
    gui.mainloop()