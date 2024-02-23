import pyqrcode
from tkinter import *

app = Tk()
app.title("Qr-code-generator")
app.geometry("400x250")

def get_entry():
    qr = pyqrcode.create(Mydata.get())
    qr.png('Mycode.png', scale=6) # scale taille dQr-code generated
    
    # Load the generated qr-code image
    qr_image = PhotoImage(file='Mycode.png') #PhotoImage : Create an image with NAME.

Mydata = StringVar()

MyLbl = Label(app, text="Write Something", font=20, pady=20)
MyLbl.pack()

MyEntry = Entry(app, textvariable=Mydata)
MyEntry.pack(pady=15, ipadx=5, ipady=5)

btna = Button(app, text="Generate QR Code", command=get_entry)
btna.pack(ipadx=7)


app.mainloop()