import PyPDF2
import sys
import argv

newFileName = argv[1]  # Ex. "newPDFName.pdf"
merger = PyPDF2.PdfFileMerger()  # pdf merger object

for file in os.listdir(os.curdir):
    print(file)
    if file.endsWith(".pdf"):
        merger.append(file)
    merger.write(newFileName)
