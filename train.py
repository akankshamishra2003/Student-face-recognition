from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("Algerian", 30, "bold"), bg="gray", fg="red")
        title_lbl.place(x=0, y=0, width=1590, height=30)

        img_top = Image.open(r"college_images\train_data1.png")
        img_top = img_top.resize((1590, 400), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=30, width=1590, height=400)

        btn = Button(self.root, text="TRAIN DATA",command=self.train_classifier, cursor="hand2",font=("times new roman",20,"bold"),bg="gray",fg="red")
        btn.place(x=0, y=430, width=1590, height=30)
 
        img_bottom = Image.open(r"college_images\train_data2.jpg")
        img_bottom = img_bottom.resize((1590, 400), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=460, width=1590, height=400)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
 
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #train classifier and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!",parent=self.root)
        
if __name__ == "__main__" :
    root = Tk()
    obj = Train(root)
    root.mainloop()