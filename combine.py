import PyPDF2
import os

def combine(pdfs, output):
    merger = PyPDF2.PdfMerger()

    for pdf in pdfs:
        if os.path.exists(pdf):
            with open(pdf, 'rb') as file:
                merger.append(file)
        else:
            print(f"File {pdf} not found, skipping.")
    
    with open(output, 'wb') as outputFile:
        merger.write(outputFile)
    
    print(f"Combined PDF saved to {output}")