from rembg import remove
from PIL import Image

input_path = input("Give the name of the image : ")
output_path = 'removed_bg.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)