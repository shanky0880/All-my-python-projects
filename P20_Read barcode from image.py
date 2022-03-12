import cv2

from pyzbar.pyzbar import decode

img = cv2.imread('qrcode.png')

for barcode in decode(img):
    print(barcode.data)
    mydata = barcode.data.decode('utf-8')
    print(mydata)
