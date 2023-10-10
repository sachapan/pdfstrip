# from PyPDF2 import PdfFileMerger, PdfFileWriter, PdfFileReader
from pypdf import PdfMerger, PdfWriter, PdfReader
import os
import argparse


def main():
    merger = PdfMerger()
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--files', type=str, nargs='+', required=True,
                        help='A space separated list of pdf file names to merge.')
    parser.add_argument('-o', '--output', type=str, required=True,
                        help='File name for merged pdf.')
    args = parser.parse_args()
    input_files = (args.files)
    output_file = (args.output)
    for input_file in input_files:
        if not os.path.isfile(input_file):
            raise("File not found.")
            exit()
        else:
            print("Processing:", input_file)
            apdf = open(input_file, "rb")
            merger.append(apdf)
    output = open(output_file, "wb")
    merger.write(output)
    print("Merge complete into file:", output_file)


if __name__ == "__main__":
    main()
