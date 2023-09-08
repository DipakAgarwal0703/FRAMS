import csv
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os

class See_Attendance_Section:
    def __init__(self,root):
        #Setting Up window form
        self.root=root
        self.root.geometry("670x100+480+390")
        self.root.title("See Attendance")      
        self.root.resizable(False,False)
        self.root.focus_force()
   
        bg_img = Label(self.root,bg="white")
        bg_img.place(x=0,y=0,relwidth=1,relheight=1)
        
        # Student Attendance Button
        start_atten=Image.open(r"Images\Student_See_Attendance.png")     
        start_atten=start_atten.resize((300,50),Image.ANTIALIAS)
        self.photostart_atten=ImageTk.PhotoImage(start_atten) 

        b1=Button(bg_img,image=self.photostart_atten,command=self.std_atndd,cursor="hand2",bd=2,relief=RIDGE,fg="white",bg="black",activeforeground="black",activebackground="black")
        b1.place(x=5,y=20,width=300,height=50)

        # Teacher Attendance Button
        save_atten=Image.open(r"Images\Teacher_See_Attendance.png")     
        save_atten=save_atten.resize((300,50),Image.ANTIALIAS)
        self.photosave_atten=ImageTk.PhotoImage(save_atten) 

        b2=Button(bg_img,image=self.photosave_atten,command=self.tch_atndd,cursor="hand2",bd=2,relief=RIDGE,fg="white",bg="black",activeforeground="black",activebackground="black")
        b2.place(x=355,y=20,width=300,height=50)
        
    def std_atndd(self):
        os.startfile("Attendance_Sheet")
        
    def tch_atndd(self):
        os.startfile("Teacher_Attendance_Sheet")

if __name__ == "__main__":
    root=Tk()
    obj=See_Attendance_Section(root)
    root.mainloop()