# (17)*********************Menus and Submenues in GUI using Python***************

from tkinter import *

root = Tk()
root.title("Pycharm")
root.geometry("1000x800")

# -----creat a function to run the menu button of file
def myfunc():
    print("This is the main menu tutorial")

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

root.mainloop()