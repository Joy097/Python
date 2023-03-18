import pyautogui
from PIL import Image # image lib to read image
from pytesseract import * #convert image to text
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

file = open ("converted_text.txt","w") #create a file


a = int(input("how many pictures you have ? : "))

for i in range (a) :
  image_1 = input("name of the image file : ")
  img_obj = Image.open(image_1)
  text = pytesseract.image_to_string(img_obj)
  file.write(text)

file.close()