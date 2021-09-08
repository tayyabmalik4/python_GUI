# (11)**************************Travel form Using checkbutton Entry Widget in GUI using python******

from tkinter import *

root = Tk()
root.geometry("644x344")

def getvals():
    print(f"your name is: {namevalue.get()}")
    print(f"your name is: {phonevalue.get()}")
    print(f"your name is: {gendervalue.get()}")
    print(f"your name is: {contactvalue.get()}")
    print(f"your name is: {paymentvalue.get()}")
    print(f"you are choosing checkbox is: {foodservicevalue.get()}")

# -----Creating Labels
Label(root, text="Welcome to Tayyab Travels",font='comixsansms 13 bold',pady=15).grid(row=0,column=3)
name = Label(root, text='Name')
phone = Label(root, text= "phone")
gender = Label(root, text= "Gender")
contact = Label(root, text="Emergency Contect")
payment = Label(root, text="Payment Mode")
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
contact.grid(row=4, column=2)
payment.grid(row=5, column=2)

# ----Now Creating the variable which we store the entries
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
contactvalue = StringVar()
paymentvalue = StringVar()
foodservicevalue = IntVar()

# -----Now Creat a Entry using Entry class for our form
nameentry =Entry(root,textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
contactentry = Entry(root, textvariable=contactvalue)
paymententry = Entry(root, textvariable=paymentvalue)

# ----Now packing the entries using grid class
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
contactentry.grid(row=4,column=3)
paymententry.grid(row=5,column=3)

# ---creating Checkbox
foodservice = Checkbutton(text="Want to prebool your meals? ",variable= foodservicevalue)
foodservice.grid(row=6,column=3)

# ----Button and packing it and assigning it a command
Button(text="Submit to Tayyab Travels",command=getvals).grid(row=7,column=3)


root.mainloop()