# (20)*********************Creating a Radio Button in GUI using Python****************************************

from tkinter import *
import tkinter.messagebox as tmsg

root= Tk()
root.geometry("455x333")
root.title("Radio Button Tutorial")

def order():
    tmsg.showinfo("Order Received",f"We have received your order for {var.get()}. Thanks for ordering.")

# var = IntVar()
var = StringVar()
var.set("Radio")
Label(root,text="What would you like to have sir?",font="lucida 19 bold", justify=LEFT, padx = 14).pack()
radio =Radiobutton(root, text="Dosa",padx=14, variable=var, value="Dosa").pack(anchor="w")
radio=Radiobutton(root, text="Idly", padx=14,variable=var,value="Idly").pack(anchor="w")
radio=Radiobutton(root,text="Paratha", padx=14, variable=var, value="paratha").pack(anchor="w")
radio=Radiobutton(root,text="Samosa",padx=14, variable=var, value="Samosa").pack(anchor="w")
Button(text="Order Now",command=order).pack(anchor="w")

root.mainloop()

