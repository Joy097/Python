import pyqrcode
import png
from pyqrcode import QRCode

qr = 'www.facebook.com'

url = pyqrcode.create(qr)
url.png('qr.png',scale=20)