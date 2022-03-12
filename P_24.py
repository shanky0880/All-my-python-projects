import tkinter as tk
from PIL import Image,ImageDraw
import numpy as np
import cv2
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\Sanjeev\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


win = tk.Tk()

w,h, = 500,500
fontButton = 'Helvetica 20 bold'

canvas = tk.Canvas(win,width=w,height=h,bg='white')
canvas.grid(row=0,column=0,columnspan=4)
count = 0

def eventFunction(event):
    x = event.x
    y = event.y
    x1 = x-20
    y1 = y-20
    x2 = x+20
    y2 = y+20

    canvas.create_oval((x1,y1,x2,y2),fill='black')
    imgDraw.ellipse((x1,y1,x2,y2),fill='white')

def save():
    global count
    imgArray = np.array(img)
    imgArray = cv2.resize(imgArray,(20,20))

    cv2.imwrite('data/'+str(count)+'.jpg',imgArray)
    count = count + 1

def predict():
    img = Image.open('data/0.jpg')
    text = tess.image_to_string(img)

    print(text)


def clear():
    canvas.delete('all')
    img = Image.new('RGB',(w,h),(0,0,0))
    imgDraw = ImageDraw.Draw(img)



buttonsave = tk.Button(win,text='Save', bg='light sea green', fg='white', font=fontButton, command = save)
buttonsave.grid(row=1,column=0)

buttonPredict = tk.Button(win,text='Predict', bg='blue', fg='white', font=fontButton, command = predict)
buttonPredict.grid(row=1,column=1)

buttonclear = tk.Button(win,text='Clear', bg='gold', fg='white', font=fontButton, command = clear)
buttonclear.grid(row=1,column=2)

buttonexit = tk.Button(win,text='Exit', bg='red', fg='white', font=fontButton)
buttonexit.grid(row=1,column=3)

labelStatus = tk.Label(win,text='Predict Value : None', bg='white', fg='black', font=fontButton)
labelStatus.grid(row=2,column=0,columnspan=4)

canvas.bind('<B1-Motion>',eventFunction)
img = Image.new('RGB',(w,h),(0,0,0))
imgDraw = ImageDraw.Draw(img)

win.mainloop()