#from PyPDF2 import PdfFileWriter, PdfFileReader
from pypdf import PdfWriter, PdfReader
import os


def Separator():
    print("------------------------------------------------------------------")


def main():
    while True:
        input_file = input("Filename to strip: ")
        if os.path.isfile(input_file):
            break
        else:
            print("No such file!")
    reader = PdfReader(input_file, 'rb')
    Separator()
    # Test for pdf with only a single page.
    #if reader.getNumPages() == 1:
    if len(reader.pages) == 1:
        print("If you wish to remove pages from a single page pdf perhaps you would prefer to delete the file.")
        exit()
    else:
        print(input_file, "has", len(reader.pages), "pages.")
    Separator()
    input_string = input(
        "Which pages would you like to remove - space separated list: ")
    output_file = (os.path.splitext(input_file)[0] + "_stripped.pdf")
    print("Output will be sent to: " + output_file)
    print("Processing.....")
    # Can we deal with comma separated automatically? 1, 3, 84
    # Can we deal with ranges? 7, 9-45
    # if ',' in input_string:
    #    pages_to_delete = list(map(int, input_string.split(',')))
    #    print(pages_to_delete)
    # exit()
    # else:
    pages_to_delete = list(map(int, input_string.split()))
    if len(pages_to_delete) > 1:
        print("Deleting pages:", str(pages_to_delete))
    else:
        print("Deleting page:", int(pages_to_delete[0]))
    # Need to decrement all pages by one because pypdf counts from zero.
    pages_to_delete = list(map(lambda x: x - 1, pages_to_delete))
    output = PdfWriter()
    for i in range(len(reader.pages)):
        if i not in pages_to_delete:
            p = reader.pages[i]
            output.add_page(p)
    with open(output_file, 'wb') as f:
        output.write(f)
    print("Strip completed.")
    outfile = PdfReader(output_file, 'rb')
    print(output_file, "has", len(outfile.pages), "page(s).")


if __name__ == "__main__":
    main()
