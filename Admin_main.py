from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
import os
from tkinter import filedialog as fd
#--------------------------------------------
from student_details import student_details
from teacher_details import teacher_details
from teacher_attendance import Teacher_Attendance_Section
from train import Train
from See_Attendance import See_Attendance_Section
from Developer import Developer_Section
from Photo_Sample import See_Photo_Section


class Admin_Section:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("FRAMS")
        self.root.resizable(False,False)
        self.root.focus_force()
        
        #Background Image
        bg1=Image.open(r"Images\Background_All.png")
        bg1=bg1.resize((1530,800))
        self.photobg1=ImageTk.PhotoImage(bg1)
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0,relwidth=1,relheight=1)
        
        # Add Student Button
        add_std=Image.open(r"Images\Add_Student.png")  #(Have to link)
        add_std=add_std.resize((300,50),Image.ANTIALIAS)
        self.photoadd_std=ImageTk.PhotoImage(add_std) 

        b1=Button(bg_img,image=self.photoadd_std,cursor="hand2",command=self.student_pannels,bd=2,relief=RIDGE,fg="white",bg="black",activeforeground="black",activebackground="black")
        b1.place(x=65,y=270,width=300,height=50)
        
        # Add Teacher Button
        add_tch=Image.open(r"Images\Add_Teacher.png")  #(Have to link)
        add_tch=add_tch.resize((300,50),Image.ANTIALIAS)
        self.photoadd_tch=ImageTk.PhotoImage(add_tch) 

        b1=Button(bg_img,image=self.photoadd_tch,cursor="hand2",command=self.teacher_pannels,bd=2,relief=RIDGE,fg="white",bg="black",activeforeground="black",activebackground="black")
        b1.place(x=65,y=330,width=300,height=50)
        
        # Train Data Button
        train_data=Image.open(r"Images\Train_Data.png")     
        train_data=train_data.resize((300,50),Image.ANTIALIAS)
        self.phototrain_data=ImageTk.PhotoImage(train_data) 

        b1=Button(bg_img,image=self.phototrain_data,command=self.train_pannels,cursor="hand2",bd=2,relief=RIDGE,fg="white",bg="black",activeforeground="black",activebackground="black")
        b1.place(x=65,y=390,width=300,height=50)
        
        # Photo Sample Button
        see_photo_std=Image.open(r"Images\Photo_Sample.png")
        see_photo_std=see_photo_std.resize((300,50),Image.ANTIALIAS)
        self.photosee_photo_std=ImageTk.PhotoImage(see_photo_std) 

        b1=Button(bg_img,image=self.photosee_photo_std,command=self.see_photos,cursor="hand2",bd=2,relief=RIDGE,fg="white",bg="black",activeforeground="black",activebackground="black")
        b1.place(x=65,y=450,width=300,height=50)
        
        # See Attendance Button
        see_atten=Image.open(r"Images\See_Attendance.png")
        see_atten=see_atten.resize((300,50),Image.ANTIALIAS)
        self.photosee_atten=ImageTk.PhotoImage(see_atten) 

        b1=Button(bg_img,image=self.photosee_atten,command=self.see_attendance,cursor="hand2",bd=2,relief=RIDGE,fg="white",bg="black",activeforeground="black",activebackground="black")
        b1.place(x=65,y=570,width=300,height=50)
        # b1.place(x=65,y=690,width=300,height=50)
        
        
        # Developer Button
        developer_btn=Image.open(r"Images\Developer.png")   #(Have to link)
        developer_btn=developer_btn.resize((300,50),Image.ANTIALIAS)
        self.photodeveloper_btn=ImageTk.PhotoImage(developer_btn) 

        b1=Button(bg_img,image=self.photodeveloper_btn,cursor="hand2",command=self.developer_pannels,bd=2,relief=RIDGE,fg="white",bg="black",activeforeground="black",activebackground="black")
        b1.place(x=65,y=630,width=300,height=50)
        
        # Mark Attendance Button
        mark_atten=Image.open(r"Images\Mark_Attendance.png")  #(Have to link)
        mark_atten=mark_atten.resize((300,50),Image.ANTIALIAS)
        self.photomark_atten=ImageTk.PhotoImage(mark_atten) 

        b1=Button(bg_img,image=self.photomark_atten,cursor="hand2",command=self.attendance_pannels,bd=2,relief=RIDGE,fg="white",bg="black",activeforeground="black",activebackground="black")
        b1.place(x=65,y=510,width=300,height=50)
        
        
        # Exit Button
        exit_btn=Image.open(r"Images\Exit.png")
        exit_btn=exit_btn.resize((300,50),Image.ANTIALIAS)
        self.photoexit_btn=ImageTk.PhotoImage(exit_btn) 

        b1=Button(bg_img,image=self.photoexit_btn,command=self.iExit,cursor="hand2",bd=2,relief=RIDGE,fg="white",bg="black",activeforeground="black",activebackground="black")
        b1.place(x=65,y=690,width=300,height=50)
 
# ==================Funtion for Open Adding Student Data==================       
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=student_details(self.new_window)
        
# ==================Funtion for Open Adding Teacher Data==================       
    def teacher_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=teacher_details(self.new_window)
        
# ==================Funtion for Open Traing Dataset==================       
    def train_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

# ==================Funtion for Marking Teacher Attendance==================       
    def attendance_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Teacher_Attendance_Section(self.new_window)
        
        
# ==================Funtion for Open Images Folder==================
    def see_photos(self):
        self.new_window=Toplevel(self.root)
        self.app=See_Photo_Section(self.new_window)
          
# ==================Functions for See Attendance Folder=====================
    def see_attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=See_Attendance_Section(self.new_window)


# ==================Functions for See About Developers=====================
    def developer_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer_Section(self.new_window)

# ==================Functions for Exit====================
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Do you want to exit",parent=self.root)
        if self.iExit>0:
            self.root.destroy()

if __name__ == "__main__":
    root=Tk()
    obj=Admin_Section(root)
    root.mainloop()
