from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="DEVELOPER", font=("Algerian", 30, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1590, height=35)

        img_top = Image.open(r"college_images\developer.jpeg")
        img_top = img_top.resize((1590, 810), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=35, width=1590, height=810)

        main_frame=Frame(f_lbl,bd=2,bg="white",)
        main_frame.place(x=1000,y=100,width=450,height=600)

        img_frame = Image.open(r"college_images\Benefits-of-facial-recognition-attendance-system.png")
        img_frame = img_frame.resize((450, 600), Image.ANTIALIAS)
        self.photoimg_frame = ImageTk.PhotoImage(img_frame)

        f_lbl = Label(main_frame, image=self.photoimg_frame)
        f_lbl.place(x=200, y=0, width=250, height=200)

if __name__ == "__main__" :
    root = Tk()
    obj = Developer(root)
    root.mainloop()