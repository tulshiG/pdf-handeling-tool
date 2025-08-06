import PyPDF2
import os
def merge_pdf(input_folder,output_pdf):
    pdf_writer=PyPDF2.PdfWriter()
    #Remove the merged exists file 
    if os.path.exists(output_pdf):
        os.remove(output_pdf)
    #Get a list of files in input folder
    pdf_files=[file for file in os.listdir(input_folder) if file.endswith('.pdf')]

    #sort the pdf files
    pdf_files.sort()

    pdf_writer=PyPDF2.PdfWriter()



    for pdf in pdf_files:
        with open(os.path.join(input_folder,pdf),'rb') as file:
            pdf_reader=PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])


        with open(output_pdf,'wb') as out:
            pdf_writer.write(out)
        #print(f"Merge Pdf saved as {output_pdf}")
input_folder="pdfpython"
output_pdf="pdfpython/merged.pdf"
merge_pdf('input_folder','output_pdf')