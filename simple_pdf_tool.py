import PyPDF2
from os import path

def merge_files(file_list):
    number_files = len(file_list)
    if number_files < 2:
        print("Please enter more than one file")
        exit(0)
    else:
        merger = PyPDF2.PdfFileMerger(False)
        for file in file_list:
            input_pdf = open(file, 'rb')
            merger.append(input_pdf)
        merger.write("merged.pdf")


def rotate_all(deg,file):
    if (deg != "90") and (deg != "180") and (deg != "270") :
        print("Please chose the right number of degrees")
        exit(0)
    input_pdf = open(file, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(input_pdf,False)
    pdf_writer = PyPDF2.PdfFileWriter()
    for pagenum in range(pdf_reader.numPages):
        page = pdf_reader.getPage(pagenum)
        page.rotateClockwise(int(deg))
        pdf_writer.addPage(page)
    output_pdf = open('rotated.pdf', 'wb')
    pdf_writer.write(output_pdf)
    output_pdf.close()
    input_pdf.close()

def rotate_pages(deg,file,page_list):   
    input_pdf = open(file, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(input_pdf,False)
    pdf_writer = PyPDF2.PdfFileWriter()
    for pagenum in range(pdf_reader.numPages):
        page = pdf_reader.getPage(pagenum)
        if str(pagenum+1) in page_list:
            page.rotateClockwise(int(deg))
        pdf_writer.addPage(page)
    output_pdf = open('rotated.pdf', 'wb')
    pdf_writer.write(output_pdf)
    output_pdf.close()
    input_pdf.close()



choice = input("What do you want to do: \n 1)Merge PDFs\n 2)Rotate PDFs")

if choice == "1":
    file_list = input("Enter the path of the different files separated by ';' :")
    file_list = file_list.strip().split(";")
    for pdf_file in file_list:
        if not path.exists(pdf_file):
            print("One or more of the file do not exist or your file list format is wrong")
            exit(0)
    merge_files(file_list)

if choice == "2":
    file = input("Enter the path of your file:")
    if not path.exists(file):
        print("This file does not exist")
        exit(0)
    page_list= input("Which pages do you want to rotate? all or x;y;z :")
    page_list = page_list.strip().split(";")
    for page in page_list:
        if not page.isdigit():
            print("Please enter the right page format")
            exit(0)
    degrees = input("How many degrees do yo want to rotate the PDF? 90, 180, 270 :")
    if (degrees != "90") and (degrees != "180") and (degrees != "270") :
        print("Please chose the right number of degrees")
        exit(0)
    if (page_list[0] == "all"):
        rotate_all(degrees,file)
        print("Done")
    else :
        rotate_pages(degrees,file,page_list)
        print("Done")

else:
    print("Not a valid choice")
    exit(0)
