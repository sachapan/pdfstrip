## pdfstrip.py


A little whacked together pdf processor to delete pages using [pyPDF2](https://github.com/mstamy2/PyPDF2).  It creates a new file and leaves the original intact.

Sample run with a two page pdf.  Sample in this repo: [sachapan_github.pdf](https://github.com/sachapan/pdfstrip/blob/main/sachapan_github.pdf).

    python3 .\pdfstrip.py
    Filename to strip: sachapan_github.pdf
    -----------------------------------------------------------------------
    sachapan_github.pdf  has  2  pages.
    -----------------------------------------------------------------------
    Pages to remove - space separated list: 2
    Output will be sent to: sachapan_github_stripped.pdf
    Processing.....
    Deleting page:  2
    sachapan_github_stripped.pdf strip completed.

A larger sample file with 99 pages: issue [114 of the MagPi magazine](https://magpi.raspberrypi.com/issues/114/pdf/download).

    python3 .\pdfstrip.py
    Filename to strip: MagPi114.pdf
    -----------------------------------------------------------------------
    MagPi114.pdf  has  100  pages.
    -----------------------------------------------------------------------
    Pages to remove - space separated list: 2 4 7
    Output will be sent to: MagPi114_stripped.pdf
    Processing.....
    Deleting pages:  [2, 4, 7]
    Strip completed.
    MagPi114_stripped.pdf has 97 pages.


