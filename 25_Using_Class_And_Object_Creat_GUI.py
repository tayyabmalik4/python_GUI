# (25)*******************************Using Class and objects To Creat GUI using python*********************************************

# ----in the class we use self as a root which we use in the simple tutorials and in the main function we use root as a window so we don't confuse and try to understand this relation
from tkinter import *
import tkinter.messagebox as tmsg

class GUI(Tk):
# ----this is creating a constructer which is helping to ease to use 
    def __init__(self):
        super().__init__()
        self.geometry("744x477")
        self.title("Using Class to Creat GUI")
# ----this is creating a fucntion to show the statusbar in the GUI
    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self, textvariable=self.var,relief=SUNKEN,anchor="w")
        self.statusbar.pack(side=BOTTOM,fill=X)

    def click(self):
        print("thanks your Response")
        tmsg.showinfo("Click","Thanks for Your Response")

    def creatbutton(self,inptext):
        Button(text = inptext,command=self.click).pack()

# ----this is the main function which we calling the GUI's function which we creat in the GUI class
if __name__=="__main__":
    window = GUI()
    window.status()
    window.creatbutton("Click me")
    window.mainloop()