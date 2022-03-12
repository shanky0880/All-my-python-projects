import cv2
from pyzbar.pyzbar import decode
import webbrowser


def scan():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    while True:
        success, img = cap.read()
        for barcode in decode(img):
           # print(barcode.data)
            mydata = barcode.data.decode('utf-8')
            webbrowser.get().open(mydata)
            print(mydata)

        cv2.imshow('Result', img)
        key = cv2.waitKey(1)
        if key == 27:
            break

    cv2.destroyAllWindows()

scan()