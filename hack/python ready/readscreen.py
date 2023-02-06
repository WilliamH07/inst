# cv2.cvtColor takes a numpy ndarray as an argument
import numpy as nm
import time
import pytesseract
  
# importing OpenCV
import cv2
  
from PIL import ImageGrab
word = 'incorrect'
  
def imToString():

    # Path of tesseract executable
    pytesseract.pytesseract.tesseract_cmd ='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    while(True):
  
        # ImageGrab-To capture the screen image in a loop. 
        # Bbox used to capture a specific area.
        cap = ImageGrab.grab(bbox =(1500, 950, 2500, 1050))# left, top, right, bottom
  
        # Converted the image to monochrome for it to be easily 
        # read by the OCR and obtained the output String.
        tesstr = pytesseract.image_to_string(
                cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY), 
                lang ='eng')
        if word in tesstr:
                print('No')

        else:
                print('YES')
        break
  
# Calling the function
time.sleep(1.5)
imToString()


