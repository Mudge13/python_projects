import PyPDF2

template = PyPDF2.PdfReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfWriter()

for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)

    with open('watermarked.pdf', 'wb') as file:
        output.write(file)

# template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
# watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
# output = PyPDF2.PdfFileWriter()

# for i in range(template.getNumPages()):
#   page = template.getPage(i)
#   page.mergePage(watermark.getPage(0))
#   output.addPage(page)

#   with open('watermarked_output.pdf', 'wb') as file:
#     output.write(file)
