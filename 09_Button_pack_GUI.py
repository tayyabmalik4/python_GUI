# (09)**********************Button Pack in Graphical User Interfarance*******************************

from tkinter import *

root = Tk()
root.geometry("655x333")

# ----creating function
def hello():
    print("Hello tkinter Button")
def name():
    print("How are you Jarviz")
frame=Frame(root,borderwidth=6,bg = 'grey',relief=SUNKEN)
frame.pack(side=LEFT,anchor='nw')

b1= Button(frame,fg='red',text='Print now',command=hello)
b1.pack(side=LEFT,padx=23)

b2 = Button(frame, fg='blue',text='this is amazing',command=name)
b2.pack(side=LEFT,padx=23)

b3 = Button(frame,fg='yellow', text = 'good work')
b3.pack(side=LEFT,padx=23)

b4 = Button(frame, fg='green',text= 'this is very fablous')
b4.pack(side=LEFT,padx=23)

root.mainloop()