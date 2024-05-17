from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from faceRecognition import FaceRecognition
from attendance import Attendance
from developer import Developer


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        #image 1
        img1 = Image.open(r"college_images\Whats-Unique-About-Our-Facial-Recognition-System.jpg")
        img1 = img1.resize((530, 150), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=530, height=150)
        
        #image 2
        img2 = Image.open(r"college_images\centre_img.jpg")
        img2 = img2.resize((530, 150), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=500, y=0, width=530, height=150)

        #image 3
        img3 = Image.open(r"college_images\Benefits-of-facial-recognition-attendance-system.png")
        img3 = img3.resize((530, 150), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=1000, y=0, width=530, height=150)

        #background image
        img4 = Image.open(r"college_images\background_img.jpeg")
        img4 = img4.resize((1590, 950), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1590, height=950)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("Algerian", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=20, width=1590, height=45)  # using .place you can place things at any part of the window

        #student button
        img5 = Image.open(r"college_images\student_btn.jpeg")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        btn1 = Button(bg_img, image=self.photoimg5,command=self.student_details, cursor="hand2")
        btn1.place(x=200, y=100, width=220, height=220)

        btn1_1 = Button(bg_img, text="Student Details",command=self.student_details, cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        btn1_1.place(x=200, y=300, width=220, height=40)

        #detect face button
        img6 = Image.open(r"college_images\facial_recognition.png")
        img6 = img6.resize((220,220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        btn1 = Button(bg_img, image=self.photoimg6, cursor="hand2",command=self.face_data)
        btn1.place(x=500, y=100, width=220, height=220)

        btn1_1 = Button(bg_img, text="Detect Face", cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"), bg="darkblue",fg="white")
        btn1_1.place(x=500, y=300, width=220, height=40)

        #Attendance button
        img7 = Image.open(r"college_images\attendance_btn.jpg")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        btn1 = Button(bg_img, image=self.photoimg7, cursor="hand2",command=self.atten_data)
        btn1.place(x=800, y=100, width=220, height=220)

        btn1_1 = Button(bg_img, text="Attendance", cursor="hand2",command=self.atten_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        btn1_1.place(x=800, y=300, width=220, height=40)

        #Help button
        img8 = Image.open(r"college_images\help.jpeg")
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        btn1 = Button(bg_img, image=self.photoimg8, cursor="hand2")
        btn1.place(x=1100, y=100, width=220, height=220)

        btn1_1 = Button(bg_img, text="Help Desk", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        btn1_1.place(x=1100, y=300, width=220, height=40)

        #Train button
        img9 = Image.open(r"college_images\train_btn.png")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        btn1 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.train_data)
        btn1.place(x=200, y=400, width=220, height=220)

        btn1_1 = Button(bg_img, text="Train Face", cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        btn1_1.place(x=200, y=600, width=220, height=40)

        #Photos button
        img10 = Image.open(r"college_images\photos.jpeg")
        img10 = img10.resize((220, 220), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        btn1 = Button(bg_img, image=self.photoimg10, cursor="hand2",command=self.open_img)
        btn1.place(x=500, y=400, width=220, height=220)

        btn1_1 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        btn1_1.place(x=500, y=600, width=220, height=40)

        #Developer button
        img11 = Image.open(r"college_images\developer_btn.jpeg")
        img11 = img11.resize((220, 220), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        btn1 = Button(bg_img, image=self.photoimg11, cursor="hand2",command=self.developer_data)
        btn1.place(x=800, y=400, width=220, height=220)

        btn1_1 = Button(bg_img, text="Developer", cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        btn1_1.place(x=800, y=600, width=220, height=40)

        # button
        img12 = Image.open(r"college_images\exit_btn.jpeg")
        img12 = img12.resize((220, 220), Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        btn1 = Button(bg_img, image=self.photoimg12, cursor="hand2")
        btn1.place(x=1100, y=400, width=220, height=220)

        btn1_1 = Button(bg_img, text="Exit", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        btn1_1.place(x=1100, y=600, width=220, height=40)

    def open_img(self):
        os.startfile("data")

        #FUNCTION(student.py)
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

        #FUNCTION(train.py)
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

        #FUNCTION(faceRecognition.py)
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=FaceRecognition(self.new_window)

        #FUNCTION(attendance.py)
    def atten_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

        #FUNCTION(developer.py)
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()