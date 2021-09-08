from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("720x480")
inp=input("Enter any Number \n")
# name=PhotoImage(file='1.png')
img= Image.open(f'img/{inp}_car.png')
name = ImageTk.PhotoImage(img)
with open(f'img\\{inp}_text.txt','r') as f:
    text = f.read()
label= Label(image=name,text= text)
# label= Label(text= text,bg='black',fg='white')
label.pack()
root.mainloop()
