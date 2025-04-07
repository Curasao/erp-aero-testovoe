
from Crypto.SelfTest.Hash.test_cSHAKE import descr
import re
from pypdf import PdfReader
import cv2
import pyzbar.pyzbar as pyzbar
from pyzbar.pyzbar import ZBarSymbol
from pyzbar.pyzbar import decode
import pymupdf
from PIL import Image
import pytest

pdf_fields = (
    'PN', 'SN', 'DESCRIPTION', 'LOCATION', 'CONDITION', 'UOM', 'DATE', 'PO', 'SOURCE', 'DATE', 'MFG', 'DOM', 'REMARK', 'BY', 'NOTES', 'Qty'
)

def test_pdf_text_fields():
    reader = PdfReader("test_task.pdf")
    page = reader.pages[0]

    text = page.extract_text(extraction_mode="layout")
    all_keys_from_pdf = re.findall(r'\w+:', text)
    cleaned_pdf_keys = tuple(map(lambda x: x.replace(":", ""), all_keys_from_pdf))

    assert cleaned_pdf_keys == pdf_fields


def test_compare_data_bar():
    reader = PdfReader("test_task.pdf")
    page = reader.pages[0]
    text = page.extract_text(extraction_mode="layout")

    lines = text.replace('  ', '\n').split('\n')

    pn_value = ''
    qty_value = ''

    for line in lines:
        if 'PN:' in line:
            pn_value = line.split(':')[1].strip()
        elif 'Qty:' in line:
            qty_value = line.split(':')[1].strip()

    pages = pymupdf.open('test_task.pdf')  # open document
    for page in pages:  # iterate through the pages
        pix = page.get_pixmap()
        # first page data
        pix.save("page.png")

    image = cv2.imread("page.png")

    decoded_list = decode(image)

    decode(Image.open('page.png'), symbols=[ZBarSymbol.DATABAR])

    pn_from_bar = decoded_list[1].data.decode("utf-8")
    qty_from_bar = decoded_list[0].data.decode("utf-8")
    assert pn_value == pn_from_bar
    assert qty_value == qty_from_bar

