from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.geometry("800x500")
root.title("Hello BG")

bg=Image.open("hello.png")

resized=bg.resize((800,500), Image.ANTIALIAS)

new_pic = ImageTk.PhotoImage(resized)
# my_bg = Label(root, image=bg)
# my_bg.place(x=0, y=0, relwidth=1, relheight=1)

my_canvas=Canvas(root)
my_canvas.pack(fill="both",expand=True)
my_canvas.create_image(0,0,image=new_pic,anchor=NW)
root.mainloop()
