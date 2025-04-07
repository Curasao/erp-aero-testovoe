import cv2
import numpy as np
from pypdf import PdfReader
import pytest

def test_decrease_resolution_picture():
    img = cv2.imread('page.png', 1)

    gray = cv2.imread('page.png', cv2.IMREAD_GRAYSCALE)
    gray_minus = np.clip(gray - 100, 0, 255).astype(np.uint8)

    cv2.imwrite("enhanced_page.png", gray_minus)
    reader = PdfReader("test_task.pdf")
    page = reader.pages[0]
    text = page.extract_text()
    print(text)