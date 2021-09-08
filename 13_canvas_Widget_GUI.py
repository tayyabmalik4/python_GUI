# (13)******************************Canvas Widget in GUI using Tkinter mofule in python*************

from tkinter import *

root = Tk()

canvas_width = 800
canvas_height = 400
root.geometry(f"{canvas_width}x{canvas_height}")
can_wedget = Canvas(root, width=canvas_width, height=canvas_height)
can_wedget.pack()

# ----To creat a line which is the points of x1,y1 to x2, y2
# can_wedget.create_line(0,0,800,400, fill= 'red')
# can_wedget.create_line(0,400,800,0, fill='red')

# ----To create a rectangular specify parameters in this order - coors of top left and coors of bootom right
# can_wedget.create_rectangle(3,5,700,300, fill='blue')

# ----if we want to creat a image in GUI than we use this method
photo=PhotoImage(file='logo.png')
can_wedget.create_image(0,0, image=photo,anchor='nw')
root.title("Tayyab Make GUI")
can_wedget.create_text(200,200,text="this is amaizing")
button=Button(root,text="Submit")
can_wedget.create_window(100,157,anchor='nw',window=button)

# -----if we want to creat a oval than we use this method
# can_wedget.create_oval(344,233,244,355)

root.mainloop() 