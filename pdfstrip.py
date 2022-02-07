from PyPDF2 import PdfFileMerger, PdfFileWriter, PdfFileReader

merger = PdfFileMerger()

input1 = open("MagPI114.pdf", "rb")
#input2 = open("document2.pdf", "rb")
#input3 = open("document3.pdf", "rb")

# print(type(input1))
#print("Pages to remove (space separated):")


def main():
    input_string = input("Pages to remove - space separated:")
    pages_to_delete = input_string.split()
    pages_to_delete = list(map(int, pages_to_delete))
    print("Deleting pages:", pages_to_delete)
#deadpage = int(input())
# print(deadpage)
#merger.append(fileobj=input1, pages=(0, (deadpage - 1)))
#merger.append(fileobj=input1, pages=(deadpage, (deadpage - 1)))


#from PyPDF2 import PdfFileWriter, PdfFileReader
# pages_to_delete = [3, 4, 5] # page numbering starts from 0
#pages_to_delete = [1, 3, 6]
    infile = PdfFileReader('MagPI114.pdf', 'rb')
    output = PdfFileWriter()

    for i in range(infile.getNumPages()):
        if i not in pages_to_delete:
            print("keeping page:", i)
            p = infile.getPage(i)
            output.addPage(p)

    with open('newfile.pdf', 'wb') as f:
        output.write(f)
#strip = [2, 4]
# for item in strip:
#    print(int(item) - 2, item)
#    merger.append(fileobj=input1, pages=(int(item) - 1, item))
# add the first 3 pages of input1 document to output - aka from 0 to 2
#merger.append(fileobj=input1, pages=(0, 2))

# insert the first page of input2 into the output beginning after the second page
#merger.merge(position=2, fileobj=input2, pages=(0, 1))
# append entire input3 document to the end of the output document
# merger.append(input3)


# Write to an output PDF document
#output = open("document-output.pdf", "wb")
# merger.write(output)
if __name__ == "__main__":
    main()
