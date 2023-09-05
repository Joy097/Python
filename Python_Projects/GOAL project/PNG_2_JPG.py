from PIL import Image

img = Image.open (r'C:\\Users\\User\\Desktop\\small python projects\\a.jpg')
img_new = img.convert('RGB')
img_new.save(r'C:\\Users\\User\\Desktop\\small python projects\\a.png',quality=95)

