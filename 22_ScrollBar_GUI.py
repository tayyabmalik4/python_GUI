# (22)*************************ScrollBar in GUI****************

from tkinter import *

root= Tk()
root.geometry("433x433")
root.title("ScrollBar")
# ----For connecting Scrollbar to a widget
# 1. wdiget(yscrollcommand=scrollbar.set())
# 2. scrollbar.config(command = widget.yview)

# ----creating scrollbar
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# listbox= Listbox(root,yscrollcommand=scrollbar.set)
# for i in range(344):
    # listbox.insert(END,f"Item {i}")
# listbox.pack(fill=X,padx=45)
# scrollbar.config(command=listbox.yview)

# -----this is for the text file we use this method
text=Text(root, yscrollcommand=scrollbar.set)
text.pack(fill=BOTH)
scrollbar.config(command=text.yview)


root.mainloop()