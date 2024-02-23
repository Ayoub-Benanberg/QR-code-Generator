import pyqrcode
from tkinter import *

app = Tk()
app.title("Qr-code-generator")
app.geometry("400x400")

def get_entry():
    qr = pyqrcode.create(Mydata.get())
    # qr.png('Mycode.png', scale=6) # scale taille dQr-code generated
    
    # Load the generated qr-code image
    qr_image = PhotoImage(file='Mycode.png') #PhotoImage : Create an image with NAME.
    
    # Updati the qr-code labl with img
    qr_label.config(image=qr_image)
    qr_label.image = qr_image
    
Mydata = StringVar()

MyLbl = Label(app, text="Write Something", font=20, pady=20)
MyLbl.pack()

MyEntry = Entry(app, textvariable=Mydata)
MyEntry.pack(pady=15, ipadx=5, ipady=5)

btna = Button(app, text="Generate QR Code", command=get_entry)
btna.pack(ipady=5, ipadx=7)

#Afficher l'Qr-code generated
qr_label = Label(app)
qr_label.pack(pady=5)

app.mainloop()