from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("633x453")
root.title("This is a Test")

def rate():
    # print("Rate us")
    rating=tmsg.showinfo("Rating",f"Thanks! Your Feedback {slider.get()}.")
    with open("19_test_rating.txt","a") as f:
        f.write(f"Thanks your Feedback {slider.get()}\n")

Label(root, text="Please Giving the Rating in 0 to 10")
slider = Scale(root, from_=0, to=10,orient=HORIZONTAL)
slider.set(5)
slider.pack()
Button(root,text= "Submit",command=rate).pack()

root.mainloop()