# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:00:30 2020

@author: fidelis.limbong
"""
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

import cv2


img = cv2.imread('plat mobilku.jpg')

ret,th = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)

text = pytesseract.image_to_string(th,config='--psm 8')

#cv2.imshow('frame',th)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

print(text)

