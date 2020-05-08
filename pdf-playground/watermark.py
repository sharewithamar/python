import PyPDF2

# source_file = open('./super.pdf', 'rb')
# watermark_file = open('./wtr.pdf', 'rb')

wtr_reader = PyPDF2.PdfFileReader(open('./wtr.pdf', 'rb'))
wtr_page = wtr_reader.getPage(0)

source_reader = PyPDF2.PdfFileReader(open('./super.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()


for i in range(source_reader.numPages):
    current_page = source_reader.getPage(i)
    current_page.mergePage(wtr_page)
    output.addPage(current_page)

# i = 0
# while i < source_reader.numPages:
#     current_page = source_reader.getPage(i)
#     current_page.mergePage(wtr_page)
#     output.addPage(current_page)
#     i = i+1


with open('draft.pdf', 'wb') as new_file:
    output.write(new_file)

# source_file.close()
# watermark_file.close()
