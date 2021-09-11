# (24)***********************StatusBar in GUI*******************************

from tkinter import *
root= Tk()
root.geometry("455x322")
root.title("Status Bar")

def upload():
    statusvar.set("Busy...")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready Now")


statusvar = StringVar()
statusvar.set("Ready")
sbar=Label(root, textvariable=statusvar, relief=SUNKEN,anchor="w")
sbar.pack(side=BOTTOM,fill=X)
Button(root,text="Upload",command=upload).pack()
root.mainloop()