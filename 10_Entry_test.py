from tkinter import *

root= Tk()
root.geometry("644x344")

def getvals():
    print(f"username is: {uservalue.get()}")
    print(f"Password is: {passwordvalue.get()}")
    print(f"you select it: {checkboxvalue.get()}")

Label(text="Welcome to the Login Page",font= 'comixsansms 13 bold').grid(row=0,column=3)
user= Label(root, text="Username: ")
password = Label(root, text="Password: ")
user.grid(row=1,column=2)
password.grid(row=2,column=2)

uservalue= StringVar()
passwordvalue = StringVar()
checkboxvalue = IntVar()

userentry = Entry(root, textvariable=uservalue)
passwordentry = Entry(root, textvariable = passwordvalue)
userentry.grid(row=1,column=3)
passwordentry.grid(row=2,column=3)

# ----creating checkbox
box= Checkbutton(text="Would you like to submit it",variable=checkboxvalue).grid(row=3,column=3)
button=Button(text="Submit Now",command=getvals).grid(row=4,column=3)

root.title("login page")
root.mainloop()
