# (05)************************Display Images in Graphical User Interfarance***********************************

# ----importing labraries
from tkinter import *
from PIL import Image, ImageTk
import os

# ----tkinter is not suppported the jpeg images so we use pillow(PIL) library to use jpeg images

# ----Starting
root = Tk()
root.geometry("1255x944")
# photo = PhotoImage(file='logo.png')

# -----for Jpg Images
 
# image = Image.open('photo.JPEG')
# photo = ImageTk.PhotoImage(image)

# -----showing the images using os module
osmod=os.fspath('D:\\machine learning practice\\python GUI\\logo.png')
photo = PhotoImage(file=osmod)

# ----Creating label to show the Image
label=Label(image=photo)
label.pack()

root.mainloop()
