# The PDF ripping and stripping saga, or how I learned to relax and use python to bend pdfs to my will.

Everyone I know seems to have a love/hate relationship with [the pdf](https://en.wikipedia.org/wiki/PDF) standard.  Graphical tools abound at various price points to create and/or manipulate existing files.  Occasionally I find myself needing to modify such files in new and exciting ways. As I have been doing lately, I pull out python from the ol' geek toolbox.  This is a (growing?) collection of scripts when I find a new pdf itch that needs scratching.

[pdfstrip](##pdfstrip.py)

[pdfmerge](##pdfmerge.py)

## pdfstrip.py

A little whacked together pdf processor to delete pages using [pyPDF2](https://github.com/mstamy2/PyPDF2).  It creates a new file and leaves the original intact.

*Motivation:* A file that can be read in two page scrolling doesn't line up page spreads properly in the pdf viewer. 

*Solution:* Write a script to strip a page or three and [voilà](https://en.wiktionary.org/wiki/voil%C3%A0) the two page view aligns correctly. 
### Example run with a small file

A sample run with a two page pdf.  

This sample file is in this repo: [sachapan_github.pdf](https://github.com/sachapan/pdfstrip/blob/main/sachapan_github.pdf)

    python3 .\pdfstrip.py
    Filename to strip: sachapan_github.pdf
    -----------------------------------------------------------------------
    sachapan_github.pdf has 2 pages.
    -----------------------------------------------------------------------
    Pages to remove - space separated list: 2
    Output will be sent to: sachapan_github_stripped.pdf
    Processing.....
    Deleting page:  2
    sachapan_github_stripped.pdf strip completed.
    sachapan_github_stripped.pdf has 1 page(s).

### A larger file being processed

A larger sample file with 100 pages: issue [114 of the MagPi magazine](https://magpi.raspberrypi.com/issues/114/pdf/download).

    python3 .\pdfstrip.py
    Filename to strip: MagPi114.pdf
    -----------------------------------------------------------------------
    MagPi114.pdf has 100 pages.
    -----------------------------------------------------------------------
    Pages to remove - space separated list: 2 4 7
    Output will be sent to: MagPi114_stripped.pdf
    Processing.....
    Deleting pages:  [2, 4, 7]
    Strip completed.
    MagPi114_stripped.pdf has 97 page(s).


## pdfmerge.py


This one generates a new pdf by combining files from a list of supplied pdfs.

    python3 .\pdfmerge.py                              
    python3 .\pdfmerge.py --help                       
    usage: pdfmerge.py [-h] -f FILES [FILES ...] -o OUTPUT

    optional arguments:
    -h, --help            show this help message and exit
    -f FILES [FILES ...], --files FILES [FILES ...]
                        A comma separated list of pdf file names to merge.
    -o OUTPUT, --output OUTPUT
                        File name for merged pdf.
    
    python3 .\pdfmerge.py -f 1.pdf, 2.pdf -o merged.pdf
    Processing: 2.pdf
    Merge complete into file: merged.pdf
