from combine import combine
from paths import getPaths

if __name__ == "__main__":
    pdfs = getPaths() 
    if pdfs:
        outputPath = input("Enter the output file path for the merged PDF: ").strip()
        combine(pdfs, outputPath)
    else:
        print("No PDF files provided.")