from tkinter import *
import random
import sqlite3
from tkinter import ttk
from tkinter import filedialog


root = Tk()
root.geometry('500x500')
root.title("Cephalometric analysis")

firstName = StringVar()
lastName = StringVar()
Age = IntVar()

f_name = firstName.get()
l_name = lastName.get()
age = Age.get()


def fileDialog():#brows an image 
    filename = filedialog.askopenfilename(initialdir="/", title="select a image", filetype=(("jpeg","*.jpg"),("All File","*.jpg")))
    label = ttk.Label(root, text="")
    label.place(x = 80, y=360)
    label.configure(text=filename)

def manualMethod():
    print('manual method')

def autoMethod():
    print('auto method')

label_0 = Label(root, text="Cephalometric analysis", width= 20, font=("bold",20))
label_0.place(x=90, y=53)#titlr of the GUI

lable_1 = Label(root, text="First Name :", width= 20, font=("bold", 10))
lable_1.place(x=80, y=130)

entry_1= Entry(root,textvar=firstName)
entry_1.place(x=240, y=130)

lable_2 = Label(root, text="Last Name :", width= 20, font=("bold", 10))
lable_2.place(x=80, y=170)

entry_2= Entry(root, textvar=lastName)
entry_2.place(x=240, y=170)

lable_3 = Label(root, text="Age :", width= 20, font=("bold", 10))
lable_3.place(x=80, y=210)

entry_3= Entry(root,textvar=Age)
entry_3.place(x=240, y=210)

lable_4 = Label(root, text="Gender :", width= 20, font=("bold", 10))
lable_4.place(x=80, y=250)

var = IntVar()
Radiobutton(root, text="Male",padx=5, variable=var, value=1).place(x=240,y=250)
Radiobutton(root, text="Female",padx=20, variable=var, value=2).place(x=295,y=250)

lable_5 = Label(root, text="Patient ID :", width= 20, font=("bold", 10))
lable_5.place(x=80, y=290)

randam_number = random.randint(1000000,9000000)#genarate random number as patient ID

lable_6 = Label(root, text=randam_number, width= 20, font=("bold", 10))
lable_6.place(x=210, y=290)

lable_7 = Label(root, text="Import Skull Image :", width= 20, font=("bold", 10))
lable_7.place(x=80, y=330)

Button(root, text="Brows", width=20, bg="brown", fg="white", command=fileDialog).place(x=240,y=330)

lable_8 = Label(root, text="Select a Mode :", width= 20, font=("bold", 10))
lable_8.place(x=80, y=400)

Button(root, text="Manual", width=10, bg="brown", fg="white", command= manualMethod).place(x=240,y=400)
Button(root, text="Auto", width=10, bg="brown", fg="white", command = autoMethod).place(x=325,y=400)


root.mainloop()