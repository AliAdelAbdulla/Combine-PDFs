def getPaths():
    paths = []
    print("Paths of the PDF files you want to merge (type 'done' when finished):")
    
    while True:
        path = input("PDF file path: ").strip()
        if path.lower() == 'done':
            break
        paths.append(path)
    
    return paths