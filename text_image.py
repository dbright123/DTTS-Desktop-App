import easygui
import numpy as np
import cv2
from PIL import Image
import pytesseract
from os import path
def Dlocate():
    
    file = easygui.fileopenbox()
    
    file = file.replace("\\","/")
    print(file)
    return file


def DImgExtract():
    x = Dlocate()
    pytesseract.pytesseract.tesseract_cmd = r"Tesseract-OCR\tesseract.exe" # Location of where the OCR is
    if(path.exists(x)):
        # rearraging program
        
        text = pytesseract.image_to_string(Image.open(x))
        
        #print("It doesn't need too much processing")

        
        #Output
        
        dtext = str(text)
        if(dtext != "" or dtext != " "):

            dtext = dtext.replace('\x0c','')
        
        print(len(dtext))
        if(len(dtext) > 0 ):
            #dtext.
            #dtext = dtext.replace("[^a-zA-Z0-9]","")
            #print(dtext)
            print("It required much processing")
            

        elif(len(dtext) == 0):
            img = cv2.imread(x, cv2.IMREAD_COLOR)
            img = cv2.blur(img, (5, 5))

            #HSV (hue, saturation, value)
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            h, s, v = cv2.split(hsv)

            #Applying threshold on pixels' Value (or Brightness)
            thresh = cv2.adaptiveThreshold(v, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

            #Finding contours
            contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

            #Filling contours
            contours = cv2.drawContours(img,np.array(contours),-1,(255,255,255),-1)

            #To black and white
            grayImage = cv2.cvtColor(contours, cv2.COLOR_BGR2GRAY)

            #And inverting it
            #Setting all `dark` pixels to white
            grayImage[grayImage > 200] = 0
            #Setting relatively clearer pixels to black
            grayImage[grayImage < 100] = 255
            #Write the temp file
            cv2.imwrite('temp.png',grayImage)
   
            #Read it with tesseract
            text = pytesseract.image_to_string(Image.open('temp.png'),config='tessedit_char_whitelist=0123456789 -psm 6 ')

            dtext = str(text)
            if(dtext != "" or dtext != " "):

                dtext = dtext.replace('\x0c','')
        else:
            print("Something went wrong")
    else:
        print("I cant locate the file you selected")

    return dtext

'''
text = str(DImgExtract())
print(text)
stext = text.split(" ")
print(stext)
'''