import PyPDF2
import pymupdf
import pdfplumber
import fitz 
#from tkinter import filedialog
#import tools

#merge pdf
def merge_pdf(pdf_list,output_path):
    pdf_writer=PyPDF2.PdfWriter()
    for pdf in pdf_list:
        pdf_reader=PyPDF2.PdfReader(pdf)
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])
    with open(output_path,'wb') as out:
        pdf_writer.write(out)
        print(f"Merge Pdf saved as {output_path}")
#merge_pdf(['courseraPrompteng.pdf','obc.pdf'],'merge.pdf')
#spliting pdf file to multiple pages
def split_pdf(pdf_path,output_dir):
    pdf_reader=PyPDF2.PdfReader(pdf_path)
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer=PyPDF2.PdfWriter()
        pdf_writer.add_page(pdf_reader.pages[page_num])
        output_path=f"{output_dir}/page_{page_num + 1}.pdf"
    with open(output_path,'wb') as out:
        pdf_writer.write(out)
    print(f"Saved {output_path}")
    
#split_pdf('merge.pdf','pdfcoll')
#Extract text from file
def extract_text(pdf_path,output_text_path):
    with pdfplumber.open(pdf_path) as pdf:
        full_text=""
        for page in pdf.pages:
            full_text+=page.extract_text()+'\n'
        
        with open(output_text_path,'w') as f:
            f.write(full_text)
        print(f"Extract text is saved as{output_text_path}")
#extract_text("courseraPrompteng.pdf","output.txt")

#image extract from pdf
def extract_images(pdf_path,output_dir):
    pdf_document=fitz.open(pdf_path)
    for page_index in range(len(pdf_document)):
        page=pdf_document.load_page(page_index)
        image_list=page.get_images(full=True)
    for img_index,img in enumerate(image_list):
        xref=img[0]
        base_image=pdf_document.extract_image(xref)
        image_bytes=base_image["image"]
        image_ext=base_image["ext"]
        image_filename=f"{output_dir}/image_{page_index+1}_{img_index+1}.{image_ext}"
        with open(image_filename,'wb') as image_file:
            image_file.write(image_bytes)
        print(f"Saved {image_filename}")
#extract_images('landscape.pdf','pic')



#creating password protected PDFs(Encrypted)
def encrypt_pdf(input_pdf,output_pdf,password):
    pdf_reader=PyPDF2.PdfReader(input_pdf)
    pdf_writer=PyPDF2.PdfWriter()
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])
    pdf_writer.encrypt(password)

    with open(output_pdf,'wb') as out:
        pdf_writer.write(out)
    print(f"Encrypted PDF file is saved as {output_pdf}")

#encrypt_pdf('merge.pdf','encrypted.pdf','pass123')
#Remove password form protected pdf
def decrypt_pdf(input_pdf,output_pdf,password):
    pdf_reader=PyPDF2.PdfReader(input_pdf)
    pdf_reader.decrypt(password)
    pdf_writer=PyPDF2.PdfWriter()
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])
    with open(output_pdf,'wb') as out:
        pdf_writer.write(out)
    print(f"Decrypted pdf file is saved as {output_pdf}")
#decrypt_pdf('encrypted.pdf','decrypted.pdf','pass123')
#Re-arranging pages in the pdf file 
def rearrange_pages(input_pdf,output_pdf,page_order):
    pdf_reader=PyPDF2.PdfReader(input_pdf)
    pdf_writer=PyPDF2.PdfWriter()
    for page_num in page_order:
        pdf_writer.add_page(pdf_reader.pages[page_num])
    with open (output_pdf,'wb') as out:
        pdf_writer.write(out)
    print(f"Rearranged PDF is saved as{output_pdf}")
#rearrange_pages('merge.pdf','rearrange.pdf',[1,0])
#Rotating Pages in the PDF (e.g. from Potrait to Landscape)
def rotate_pages(input_pdf,output_pdf,rotation):
    pdf_reader=PyPDF2.PdfReader(input_pdf)
    pdf_writer=PyPDF2.PdfWriter()
    for page_num in range(len(pdf_reader.pages)):
        page=pdf_reader.pages[page_num]
        page.rotate(rotation)
        pdf_writer.add_page(page)
    with open(output_pdf,'wb') as out:
        pdf_writer.write(out)
    print(f"New PDF is saved as {output_pdf}")
#rotate_pages('merge.pdf','landscape.pdf',90)
#Read metadata of the PDF file.
def read_metadata(pdf_file):
    pdf_reader=PyPDF2.PdfReader(pdf_file)
    metadata=pdf_reader.metadata
    print("Metadata of the PDF file is: ")
    for key,value in metadata.items():
        print(f"{key}:{value}")
    
#read_metadata('merge.pdf')
#add Metadata to pdf file(title,Author ,etc)
def add_metadata(input_file,output_file,title,author):
    pdf_reader=PyPDF2.PdfReader(input_file)
    pdf_writer=PyPDF2.PdfWriter()
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])
    metadata={'/Title':title,'/Author':author,'/Producer':''}
    pdf_writer.add_metadata(metadata)
    with open(output_file,'wb') as out:
        pdf_writer.write(out)
    print(f"PDF file with updated metadata is saved as {output_file}")
#add_metadata('merge.pdf','metadata_add.pdf','Sample for pdf','Tulshi')
#read_metadata('metadata_add.pdf')

#Optimise the size of  the PDF file(comperisng PDF file).
def optimise_pdf(input_file,output_file):
    pdf_document=fitz.open(input_file)
    pdf_document.save(output_file,garbage=3,deflate=False)
    print(f"Optimized PDF is saved as {output_file}")

#optimise_pdf('merge.pdf','optimise.pdf')
def split_pdf(self):
    input_pdf_path = self.input_file_entry.get()
    output_dir = filedialog.askdirectory()  # Assuming you want to prompt for an output directory
    split_pdf(input_pdf_path, output_dir)

