# (08)*********************Frames in Tkinter in Graphical User Interfarance**********************

from tkinter import *

root = Tk()
root.geometry("655x333")
f1 = Frame(root,bg='grey',borderwidth=6,relief = SUNKEN)
f1.pack(side=LEFT, fill='y')

f2 = Frame(root,borderwidth=8,bg='grey',relief=SUNKEN)
f2.pack(side=TOP,fill=X)

l=Label(f1,text="Project Tkinter - Pycharm")
l.pack(pady=142)

l2=Label(f2,text='Welcome to Sublime Text-Editor',font='Helvetica 16 bold', fg= 'red')
l2.pack()
root.mainloop()