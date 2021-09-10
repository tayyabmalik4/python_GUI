# (19)********************Slider in tkinter in GUI*********************************

from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("455x233")
root.title("Slider")

def getdollar():
    print(f"We have credited {myslider2.get()} dollers to your bank account")
    tmsg.showinfo("Dollers",f"We have credited {myslider2.get()} dollers to your bank account")


# ----this is the vertical scale
# myslider = Scale(root, from_=0, to= 100)
# myslider.pack()

# ----this is the horizontal scaler
Label(root,text="How many dollers do you want?",font="bold").pack()
myslider2=Scale(root, from_=0,to=100, orient=HORIZONTAL,tickinterval=50)
myslider2.set(10)
myslider2.pack()
Button(root,text="Get Dollers!",pady=10,command=getdollar).pack()

root.mainloop()