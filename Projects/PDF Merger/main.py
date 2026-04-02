from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs = []
n = int(input("enter the no. of Pdf to be merged\n"))

for i in range (0, n):
    name = input((f"enter the name of the PDF: {i + 1}:"))
    pdfs.append(name)


for pdf in pdfs:
    merger.append(pdf)

merger.write("final.pdf")
merger.close()