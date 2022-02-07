from PyPDF2 import PdfFileWriter, PdfFileReader
import os


def separator():
    print("-----------------------------------------------------------------------")


def main():
    while True:
        input_file = input("Filename to strip: ")
        if os.path.isfile(input_file):
            break
        else:
            print("No such file!")
    infile = PdfFileReader(input_file, 'rb')
    #print("Number of pages in file: ", input_file)
    separator()
    print(input_file, " has ", infile.getNumPages(), " pages.")
    separator()
    input_string = input("Pages to remove - space separated list: ")
    output_file = (os.path.splitext(input_file)[0] + "_stripped.pdf")
    print("Output will be sent to: " + output_file)
    print("Processing.....")
    # Can we deal with comma separated automatically? 1, 3, 84
    # Can we deal with ranges? 7, 9-45
    pages_to_delete = list(map(int, input_string.split()))
    if len(pages_to_delete) > 1:
        print("Deleting pages: ", str(pages_to_delete))
    else:
        print("Deleting page: ", input_string[0])
    pages_to_delete = list(map(lambda x: x - 1, pages_to_delete))
    output = PdfFileWriter()
    for i in range(infile.getNumPages()):
        if i not in pages_to_delete:
            p = infile.getPage(i)
            output.addPage(p)
    with open(output_file, 'wb') as f:
        output.write(f)
    print(output_file, "strip completed.")


if __name__ == "__main__":
    main()
