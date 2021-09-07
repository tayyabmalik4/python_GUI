# (04)************************Labels, Geomatry, Min and Max in python******************************

# -----Labels----labels means which we instructed the GUI and we want to write in the GUI  
# -----geomatry means we say GUI the height and wight when open the GUI
# -----minsize---the minmum size of the GUI
# -----maxsize---the maximum size of the GUI

from tkinter import *

root=Tk()

# ---- weight x height
root.geometry("733x434") 

# ---- width x height
root.minsize(300,100)
root.maxsize(1200,980)
labl= Label(text="this is the first step To Creating GUI")
labl.pack()
root.mainloop()