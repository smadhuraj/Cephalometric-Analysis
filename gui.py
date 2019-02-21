from tkinter import *
import random
import sqlite3
from tkinter import ttk
from tkinter import filedialog
import cv2
import numpy as np
import imutils
from scipy.ndimage import rotate
from matplotlib import pyplot as plt
from canny import Newclass
from mainClass import Main
from manual import Manual

root = Tk()
root.geometry('500x600')
root.title("Cephalometric analysis")

firstName = StringVar()
lastName = StringVar()
Age = IntVar()

f_name = firstName.get()
l_name = lastName.get()
age = Age.get()

sna = IntVar()
snb = IntVar()

# img = cv2.imread('scull.jpg',0)# read the X ray image in gray scale
# img_1 = cv2.imread('scull.jpg',1)
# edges = cv2.Canny(img,100,200) # apply Canny filter to loded image

# # cannyClass = Canny()

path = StringVar()

def update_vars(ssna, ssnb):
    sna.set(round(ssna))
    snb.set(round(ssnb))

def fileDialog(path):#brows an image 
    filename = filedialog.askopenfilename(initialdir="/", title="select a image", filetype=(("jpeg","*.jpg"),("All File","*.jpg")))  
    path.set(filename)  
    label = ttk.Label(root, text="")
    label.place(x = 80, y=360)
    label.configure(text=filename)

def manualMethod():
    Manual.xxx(update_vars)
    
    

def autoMethod(path):
    newPath = path.get()
    Main.mainMehod(newPath)

Button(root, text="Help", width=10, bg="blue", fg="white").place(x=0,y=0)


label_0 = Label(root, text="Cephalometric Analysis", width= 20, font=("bold",20))
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

Button(root, text="Browse", width=20, bg="blue", fg="white", command=lambda: fileDialog(path)).place(x=240,y=330)

lable_8 = Label(root, text="Select a Mode :", width= 20, font=("bold", 10))
lable_8.place(x=80, y=400)

Button(root, text="Manual", width=10, bg="blue", fg="white", command= manualMethod).place(x=240,y=400)
Button(root, text="Auto", width=10, bg="blue", fg="white", command = lambda: autoMethod(path)).place(x=325,y=400)

label_9 = Label(root, text="Result", width= 10, font=("bold",20))
label_9.place(x=90, y=440)
label_19 = Label(root, text="(press any key to show result after 4 click)", width= 40, font=("bold",8))
label_19.place(x=240, y=445)

lable_10 = Label(root, text="Angle", width= 20, font=("bold", 10))
lable_10.place(x=80, y=480)
lable_11 = Label(root, text="AVG", width= 20, font=("bold", 10))
lable_11.place(x=180, y=480)
lable_12 = Label(root, text="Actual", width= 20, font=("bold", 10))
lable_12.place(x=280, y=480)
lable_13 = Label(root, text="SNA", width= 20, font=("bold", 10))
lable_13.place(x=80, y=520)
lable_14 = Label(root, text="SNB", width= 20, font=("bold", 10))
lable_14.place(x=80, y=560)
lable_15 = Label(root, text="82", width= 20, font=("bold", 10))
lable_15.place(x=180, y=520)
lable_16 = Label(root, text="80", width= 20, font=("bold", 10))
lable_16.place(x=180, y=560)
lable_17 = Label(root, textvariable=sna, width= 20, font=("bold", 10))
lable_17.place(x=280, y=520)
lable_18 = Label(root, textvariable=snb, width= 20, font=("bold", 10))
lable_18.place(x=280, y=560)

root.mainloop()