from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox

class Train:

    def __init__(self,root):
        self.root=root
        self.root.geometry("670x60+480+390")
        self.root.title("Train Panel")
        self.root.resizable(False,False)
        self.root.focus_force()

        # Background Setting
        bg_img = Label(self.root,bg="white")
        bg_img.place(x=0,y=0,relwidth=1,relheight=1)

        # Create buttons below the section 
        # Student Train Data Button
        train_std_data=Image.open(r"Images\Train_Student_Data.png")     
        train_std_data=train_std_data.resize((300,50),Image.ANTIALIAS)
        self.phototrain_std_data=ImageTk.PhotoImage(train_std_data) 

        b1=Button(bg_img,image=self.phototrain_std_data,command=self.student_train_classifier,cursor="hand2",bd=2,relief=RIDGE,fg="white",bg="black",activeforeground="black",activebackground="black")
        b1.place(x=5,y=5,width=300,height=50)

        # Teacher Train Data Button
        train_tch_data=Image.open(r"Images\Train_Teacher_Data.png")     
        train_tch_data=train_tch_data.resize((300,50),Image.ANTIALIAS)
        self.phototrain_tch_data=ImageTk.PhotoImage(train_tch_data) 

        b2=Button(bg_img,image=self.phototrain_tch_data,command=self.teacher_train_classifier,cursor="hand2",bd=2,relief=RIDGE,fg="white",bg="black",activeforeground="black",activebackground="black")
        b2.place(x=355,y=5,width=300,height=50)


    # ==================Create Function of Traing Dataset of Student===================
    def student_train_classifier(self):
        data_dir=("StudentPhotoSample")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # conver in gray scale 
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)
        if len(faces)==0:
            messagebox.showerror("Error","No images to train")
        else:
            #=================Train Classifier=============
            clf= cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces,ids)
            clf.write("classifier.xml")

            cv2.destroyAllWindows()
            messagebox.showinfo("Result","Training Dataset Completed!",parent=self.root)
            self.root.destroy()
        
        
    # ==================Create Function of Traing Dataset of Teacher===================
    def teacher_train_classifier(self):
        data_dir=("TeacherPhotoSample")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # conver in gray scale 
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)
        if len(faces)==0:
            messagebox.showerror("Error","No images to train")
        else:        
            #=================Train Classifier=============
            clf= cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces,ids)
            clf.write("classifier.xml")

            cv2.destroyAllWindows()
            messagebox.showinfo("Result","Training Dataset Completed!",parent=self.root)
            self.root.destroy()




if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()