from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\Sanjeev\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
from PIL import Image


root = Tk()

root.title('Image Processing')
root['bg'] = 'black'
root.geometry('470x520')


#root.iconbitmap('C:\Users\Sanjeev\PycharmProjects\opencvpythonProject2\lena.jpg')
#root.geometry('520x500')

def browseFiles():
    global img



    root.filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.jpg*"),
                                                     ("all files",
                                                      "*.*")))


    img = ImageTk.PhotoImage(Image.open(root.filename))
    panel = Label(root, image=img)
    panel.pack(side="top", fill="both", expand="no")



def predict():


    text = tess.image_to_string(root.filename)

    print(text)

    labelframe = LabelFrame(root, text="Prediction Output of Image into Text : " , font=('Railways', 12, 'bold'))
    var = StringVar()
    var.set(text)
   # Label(labelframe, textvariable=var).pack()

    out = Message(labelframe, textvariable=var, bg='lavender', fg='black')
    out.config(font=("Century Gothic", 10, 'bold'))
    out.pack(side='top', fill='both', expand='yes')

    labelframe.pack(fill="both", expand="yes")


w = Label(root, text="Machine Learning Project", font=('Railways', 15, 'bold'),fg='black',bg="yellow")
w.pack(fill='x')
z = Label(root, text="Detect Text/Digits from Image", font=('Railways', 24, 'bold'),fg='black',bg="grey")
z.pack(fill='x')

btn = Button(root, text='Upload Image', font=('railways', 10, 'bold'),bg='blue', fg='white', command=browseFiles).pack(fill='y', expand='no')

btn2 = Button(root, text='Predict Value', font=('railways', 10, 'bold'),bg='red', fg='white', command=predict).pack(fill='y', expand='no')



root.mainloop()