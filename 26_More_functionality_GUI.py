# (26)**********************More funtions in GUI*******************************

from tkinter import *
root = Tk()
root.geometry("1000x780")
root.title("CodeWithTayyab - Title of My GUI")
root.wm_iconbitmap("Excercises/img/2.ico")
root.configure(background='grey')

# ----when we retrive the width and height we use this fucntion
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(f"{width}x{height}")

# -----root.destroy is to use the clossing the window
Button(text="Close",command=root.destroy).pack()

root.mainloop()
