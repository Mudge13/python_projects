import PyPDF2

with open('wtr.pdf', 'rb') as watermark_file:
    wtr_reader = PyPDF2.PdfReader(watermark_file)
    watermark = wtr_reader.pages[0]

    # open super and loops through its pages
    with open('super.pdf', 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        pages = reader.pages
        writer = PyPDF2.PdfWriter()
        # merge watermark with mages
        for i in range(len(pages)):
            page = pages[i]
            page.merge_page(watermark)
            writer.add_page(page)

        with open('watermarked.pdf', 'wb') as new_file:
            writer.write(new_file)
