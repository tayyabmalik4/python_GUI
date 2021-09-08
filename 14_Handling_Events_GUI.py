# (14)************************Handling Events in GUI using Python*****************

from tkinter import *

# ----Creating function to handle the events
def tayyab(event):
    print(f"You clicked on the button at {event.x}, {event.y}")

root= Tk()
root.title("Events in Tkinter")
root.geometry("644x334")

# ----Creating event
# ----for creating event first of all we creat button
widget=Button(root, text="Click me Please")
widget.pack()

# ----starting event
widget.bind("<Button-1>",tayyab)
# ----if we want to exit the GUI by clicking double press on the button
widget.bind("<Double-1>",quit)

root.mainloop()