from tkinter import *
from PIL import ImageTk,Image
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import webbrowser
import pyttsx3

#img = cv2.imread('qrcode.png')
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
speaker = pyttsx3.init()
class Widget:               #GUI OF VIRTUAL ASSISTAND AND COMMANDS GIVEN
    def __init__(self):
        
        root = Tk()

        root.title('Qr & Bar code Detector')
        root.geometry('520x320')

        img = ImageTk.PhotoImage(Image.open('mobile.jpg'))
        panel = Label(root, image=img)
        panel.pack(side='right', fill='both', expand='no')

        compText = StringVar()
        userText = StringVar()

        userText.set('Your Qr & Bar code Detector')
        userFrame = LabelFrame(root, text='Detector', font=('Railways', 10, 'bold'))
        userFrame.pack(fill='both', expand='yes')

        top = Message(userFrame, textvariable=userText, bg='blue', fg='white')
        top.config(font=("Century Gothic", 15, 'bold'))
        top.pack(side='top', fill='both', expand='yes')

        # compFrame = LabelFrame(root, text="Lena", font=('Railways', 10, 'bold'))
        # compFrame.pack(fill="both", expand='yes')

        btn = Button(root, text='Detect', font=('railways', 10, 'bold'), bg='purple', fg='white', command=self.clicked).pack(fill='x', expand='no')
        btn1 = Button(root, text='Scan & Search', font=('railways', 10, 'bold'), bg='Cyan', fg='Black',
                     command=self.click).pack(fill='x', expand='no')
        btn2 = Button(root, text='Close', font=('railways', 10, 'bold'), bg='black', fg='red', command=root.destroy).pack(
            fill='x', expand='no')
        root.mainloop()

    def clicked(self):
        while True:

            success, img = cap.read()
            for barcode in decode(img):
                # print(barcode.data)
                mydata = barcode.data.decode('utf-8')
                print(mydata)
                pts = np.array([barcode.polygon], np.int32)
                pts = pts.reshape((-1, 1, 2))
                cv2.polylines(img, [pts], True, (255, 0, 255), 5)
                pts2 = barcode.rect
                cv2.putText(img, mydata, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)

            cv2.imshow('Result', img)
            key = cv2.waitKey(1)
            if key == 27:
                break

        cv2.destroyAllWindows()

    def click(self):
        while True:

            success, img = cap.read()
            for barcode in decode(img):
                # print(barcode.data)
                mydata = barcode.data.decode('utf-8')
                print(mydata)
                pts = np.array([barcode.polygon], np.int32)
                pts = pts.reshape((-1, 1, 2))
                cv2.polylines(img, [pts], True, (255, 0, 255), 5)
                pts2 = barcode.rect
                cv2.putText(img, mydata, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)

                webbrowser.get().open(mydata)
                speaker.say('Here is what i found')
                speaker.runAndWait()
            cv2.imshow('Result', img)
            key = cv2.waitKey(1)
            if key == 27:
                break

        cv2.destroyAllWindows()

if __name__== '__main__':
    widget = Widget()

