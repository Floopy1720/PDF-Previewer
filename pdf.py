# Made by Floppy#6269
import os
from PyPDF2 import PdfFileReader, PdfFileWriter
import fitz
import math

def pdf_splitter(path):
    #Getting File Name
    fname = os.path.splitext(os.path.basename(path))[0]
    # Page 0 means the 1st page
    page = 0
    pdf = PdfFileReader(path)
    pdf_writer = PdfFileWriter()
    pdf_writer.addPage(pdf.getPage(page))
 
    output_filename = 'file_done.pdf'
 
    with open(output_filename, 'wb') as out:
        pdf_writer.write(out)
    print('PDF Created!')
    pass

def img(path):
    pdffile = path
    doc = fitz.open(pdffile)
    page = doc.loadPage(0)  # number of page
    pix = page.get_pixmap()
    output = "file.jpg"
    pix.save(output) 
    pass


def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

