
import barcode
from barcode.writer import ImageWriter

num = input("enter the code to generate barcode : ")
barcode_format = barcode.get_barcode_class('upc') 
# upc format has to be 11 digit
Barcode = barcode_format(num,writer=ImageWriter())
Barcode.save("generated_barcode")
