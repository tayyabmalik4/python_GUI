# (18)*************************  Show message with the help of build in function in GUI********************************

from tkinter import *
import tkinter.messagebox as tmsg 

root = Tk()

root.title("Show Message")

root.geometry("1000x800")

# -----creat a function to run the menu button of file
def myfunc():
    print("This is the main menu tutorial")

def help():
    print("This is the help function")
    # a= tmsg.showinfo("Help","Tayyab is help you with this GUI")
    # print(a)
    ok=tmsg.askyesnocancel("Cancal","Can you Rate us in playstoe")
    print(ok)

def rate():
    print("This is Rate us function")
    value = tmsg.askquestion("Experience","You Use this GUI... Was your experience Good?")
    print(value)
    if value=="yes":
        msg = "Great. Rate us on appstore please"
    else:
        msg = "Tell us what went wrong. We will call you soon"
    tmsg.showinfo("Experience", msg)
def noor():
    ans=tmsg.askretrycancel("Mahnoor sa dosti kar lo", "Soory mahnoor nahi bana gi apki dost")
    if ans:
        # print("Retry krna pe bhi kuch nahi hoga")
        tmsg.showwarning("Retry","Bhai bht marr para ge bach jao")
    else:
        print("Bahut badiya bhai cancle kar diya warna pitte")
        tmsg.showerror("Cancle","Tum sa na ho ga bhai apna kam kro")


# -----Use these to creat a non-dropdown menu
# mymenu = Menu(root)
# mymenu.add_command(label="File",command=myfunc)
# mymenu.add_command(label="Exit",command=quit)
# # ----for packing the menus we use config function
# root.config(menu=mymenu)

# ----starting the dropdown menu
mainmenu=Menu(root)
m1 = Menu(mainmenu,tearoff=0)
m1.add_command(label="New project",command=myfunc)
m1.add_command(label="Save",command=myfunc)
m1.add_separator()
m1.add_command(label="Save As",command=myfunc)
m1.add_command(label="Print",command=myfunc)
root.config(menu=mainmenu)

mainmenu.add_cascade(label="File",menu=m1)

# -----this is the 2nd mainmenu
m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut",command=myfunc)
m2.add_command(label="Copy",command=myfunc)
m2.add_separator()
m2.add_command(label="Paste",command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit",menu=m2)

# -----Starting show message menu
m3=Menu(mainmenu, tearoff=0)
m3.add_command(label="Help",command=help)
m3.add_command(label="Rate Us",command=rate) # ----for showing the message when we run this command
m3.add_command(label="Mahnoor",command=noor)
mainmenu.add_cascade(label="Help",menu=m3)
root.config(menu=mainmenu)

root.mainloop()