from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
import os
from tkinter import filedialog as fd
# ----------------------------------------
from attendance import Attendance_Section
# from StudentDetails import student_details
# from train import Train
# from FaceAttendance import facerecognitionsystem
# from developer import Developer
# from helpsupport import Helpsupport

class Teacher_Section:
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

        # Mark Attendance Button
        mark_atten=Image.open(r"Images\Mark_Attendance.png")  #(Have to link)
        mark_atten=mark_atten.resize((300,50),Image.ANTIALIAS)
        self.photomark_atten=ImageTk.PhotoImage(mark_atten) 

        b1=Button(bg_img,image=self.photomark_atten,cursor="hand2",command=self.attendance_pannel,bd=2,relief=RIDGE,fg="white",bg="black",activeforeground="black",activebackground="black")
        b1.place(x=65,y=350,width=300,height=50)
        
        # See Attendance Button
        see_atten=Image.open(r"Images\See_Attendance.png")
        see_atten=see_atten.resize((300,50),Image.ANTIALIAS)
        self.photosee_atten=ImageTk.PhotoImage(see_atten) 

        b1=Button(bg_img,image=self.photosee_atten,command=self.atndd,cursor="hand2",bd=2,relief=RIDGE,fg="white",bg="black",activeforeground="black",activebackground="black")
        b1.place(x=65,y=410,width=300,height=50)
        
        # Exit Button
        exit_btn=Image.open(r"Images\Exit.png")
        exit_btn=exit_btn.resize((300,50),Image.ANTIALIAS)
        self.photoexit_btn=ImageTk.PhotoImage(exit_btn) 

        b1=Button(bg_img,image=self.photoexit_btn,command=self.iExit,cursor="hand2",bd=2,relief=RIDGE,fg="white",bg="black",activeforeground="black",activebackground="black")
        b1.place(x=65,y=470,width=300,height=50)
        
        
# ==================Functions for Start Attendance====================
    def attendance_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance_Section(self.new_window)

 
        
# ==================Functions for See Attendance Folder=====================
    def atndd(self):
        os.startfile("Attendance_Sheet")

# ==================Functions for Exit====================
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Do you want to exit",parent=self.root)
        if self.iExit>0:
            self.root.destroy()


            
            
if __name__ == "__main__":
    root=Tk()
    obj=Teacher_Section(root)
    root.mainloop()