import PyPDF2

with open("dummy.pdf", "rb") as file:
    print(file)
    reader = PyPDF2.PdfReader(file)
    # print(len(reader.pages))
    # print(reader.pages[0])
    page = reader.pages[0]
    page.rotate(90)

    with open("tilt.pdf", "wb") as file2:
        writer = PyPDF2.PdfWriter()
        writer.add_page(page)
        writer.write(file2)
        print("DONE")
