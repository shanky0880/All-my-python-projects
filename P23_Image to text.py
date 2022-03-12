import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\Sanjeev\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
from PIL import Image

img = Image.open('text iamge.jpg')
text = tess.image_to_string(img)

print(text)