# (06)***************************Attributes of Label pack in Graphical user interfarance in python***************

from tkinter import *

root = Tk()
root.geometry("444x222")
root.title("My GUI With Tayyab")

# -----these are the attributes of label----which we use in the GUI
# ----Important Label options
# --(1)-text - add the Text
# --(2)-bd   - background
# --(3)-fg   - forground
# --(4)-font - sets the Font
    # (i)-font=('comicsansms',9,'bold')   (ii)-font='comicsansms 9 italic'
# --(5)-padx - x padding
# --(6)-pady - y padding
# --(7)-relief- border styling - SUNKEN, RAISED, GROOVE, RIDGE
label = Label(text = '''Abdul Rashid Salim Salman Khan (27 December 1965) \nis an Indian actor, film producer, singer, painter[5] and television personality who works in Hindi \nfilms. In a film career spanning over thirty years, Khan has received numerous awards, including two \nNational Film Awards as a film producer, and two Filmfare Awards for acting. He is cited in the \nmedia as one of the most commercially successful actors of Indian cinema. Forbes included him \nin their 2015 list of Top-Paid 100 Celebrity Entertainers in the world; Khan tied with Amitabh \nBachchan for No. 71 on the list, both with earnings of $33.5 million.[9][10] According to the Forbes \n2018 list of Top-Paid 100 Celebrity Entertainers in world, Khan was the highest-ranked Indian with \n82nd rank with earnings of $37.7 million.  He is also known as the host of the reality show, \nBigg Boss since 2010''', bg = 'red',fg= 'white',padx=113,pady=94,font='comicsansms 9 italic',borderwidth=3,relief=SUNKEN )


# ----these are the attributes of pack option----which we use in the GUI
# ----Important pack options
# ---(1)-anchor= NW
# ---(2)-side= top,bottom,left,right
# ---(3)-fill
# ---(4)-padx
# ---(5)-pady
# label.pack(side=BOTTOM, anchor='sw',fill=X)
label.pack(side=LEFT,fill=Y,padx=77,pady=88)



root.mainloop()