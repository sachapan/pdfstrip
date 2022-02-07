from PyPDF2 import PdfFileMerger, PdfFileWriter, PdfFileReader
import os


def main():
    while True:
        input_file = input("Filename to strip:")
        if os.path.isfile(input_file):
            break
        else:
            print("No such file!")
    output_file = (os.path.splitext(input_file)[0] + "_stripped.pdf")
    print("Output will be sent to: " + output_file)
    input_string = input("Pages to remove - space separated list: ")
    pages_to_delete = list(map(int, input_string.split()))
    print("Deleting pages:", pages_to_delete)
    pages_to_delete = list(map(lambda x: x - 1, pages_to_delete))
    infile = PdfFileReader(input_file, 'rb')
    output = PdfFileWriter()
    for i in range(infile.getNumPages()):
        if i not in pages_to_delete:
            p = infile.getPage(i)
            output.addPage(p)
    with open(output_file, 'wb') as f:
        output.write(f)
    print(output_file, "Completed.")


if __name__ == "__main__":
    main()
