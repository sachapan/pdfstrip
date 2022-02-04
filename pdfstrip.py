from PyPDF2 import PdfFileMerger

merger = PdfFileMerger()

input1 = open("MagPI114.pdf", "rb")
#input2 = open("document2.pdf", "rb")
#input3 = open("document3.pdf", "rb")

# print(type(input1))

# exit()

merger.append(fileobj=input1, pages=(0, 2))

# insert the first page of input2 into the output beginning after the second page
#merger.merge(position=2, fileobj=input2, pages=(0, 1))

# append entire input3 document to the end of the output document
# merger.append(input3)

# Write to an output PDF document
output = open("document-output.pdf", "wb")
merger.write(output)
