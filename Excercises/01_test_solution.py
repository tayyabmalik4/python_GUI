from tkinter import *
from PIL import Image, ImageTk

def every_100(text):
    final_text = ''
    for i in range(0,len(text)):
        final_text+=text[i]
        if i%100==0 and i!=0:
            final_text += "\n"
    return final_text

root = Tk()
root.title("CodeWithTayyab News - Apka apna Akhbar")
root.geometry("1000x1000")

texts= []
photos = []
for i in range(0,3):
    with open(f"img/{i+1}_text.txt") as f:
        text=f.read()
        texts.append(every_100(text))
    image = Image.open(f"img/{i+1}_car.png")
    # ----TODO:for resize these images
    image = image.resize((225,265), Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))
    
f0 = Frame(root, width=800, height=70)
Label(f0, text='Code With Harry News',font='lucida 33 bold').pack()
Label(f0, text='Sebtember 09,  2021',font= "lucida 13 bold").pack()
f0.pack()
for i in range(1,3):
    f1 = Frame(root,width=900,height=200)
    Label(f1,text=texts[i],padx=22,pady=22).pack(side='left')
    Label(f1, image=photos[i],anchor='e').pack()
    f1.pack(anchor='w')
    i=i+1
# f2 = Frame(root,width=900,height=200,pady=14,padx=22)
# Label(f2,text=texts[1],padx=22,pady=22).pack(side='right')
# Label(f2, image=photos[1],anchor='e').pack()
# f2.pack(anchor='w')
# f3 = Frame(root,width=900,height=200)
# Label(f3,text=texts[2],padx=22,pady=22).pack(side='left')
# Label(f3, image=photos[2],anchor='e').pack()
# f3.pack(anchor='w')
root.mainloop()