# resize the window
from tkinter import *

root = Tk()

root.title("Resize Window")
root.geometry("433x343")
def resize():
    print(f"The Width is: {widthvalue.get()}")
    print(f"The Height is: {heightvalue.get()}")
    root.geometry(f"{widthvalue.get()}x{heightvalue.get()}")

# f=Frame(root, borderwidth=3,relief=SUNKEN)
# f.pack(side='left',padx=3)
Label(root,text="Welcome to Resize GUI Excersize",font='comixsansms 16 bold').grid(row=0,column=3)
width=Label(root, text="Enter Your Width").grid(row=1,column=2)
height=Label(root,text="Enter Your Height").grid(row=2,column=2)

widthvalue= StringVar()
heightvalue= StringVar()

widthentry=Entry(root,textvariable= widthvalue).grid(row=1,column=3)
heightentry=Entry(root,textvariable=heightvalue).grid(row=2,column=3)

b=Button(text="Submit Now",command=resize)
b.grid(row=3,column=3)


root.mainloop()