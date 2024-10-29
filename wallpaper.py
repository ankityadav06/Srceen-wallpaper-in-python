from tkinter import *
import os
from PIL import ImageTk,Image
import os


def rotate_image():
    global cout
    img_lable.config(image=img_array[cout%len(img_array)])
    cout=cout+1




cout=1


w=Tk()
w.title("wallpaper")#title add


w.config(bg="#212121")
w.geometry("300x425")
w.resizable(False, False)

files=os.listdir("images")


img_array=[]    
for file in files:
    img=Image.open(os.path.join("images",file))
    resized_img=img.resize((220,320))
    img_array.append(ImageTk.PhotoImage(resized_img))



img_lable=Label(w,image=img_array[0])
img_lable.pack(pady=(20,10))


done_button=Button(w,text="Next",bg="white",font=("Calibri (Body) ",10),command=rotate_image)
done_button.place(y=370,height=20,width=80,x=110)



w.mainloop()