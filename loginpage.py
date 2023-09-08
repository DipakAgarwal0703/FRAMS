from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
from tkinter import messagebox
from teacher_login import Teacher_Login
from admin_login import Admin_Login

import os

class Login_Page:
    def __init__(self,root):
        self.root = root
        # print ("hello")  
        self.root.geometry("1530x800+0+0")
        self.root.title("FRAMS")
        self.root.resizable(False,False)
        self.root.focus_force()

        
        # Background Image
        bg1=Image.open(r"Images\Background_All.png")
        bg1=bg1.resize((1530,800))
        self.photobg1=ImageTk.PhotoImage(bg1)
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0,relwidth=1,relheight=1)
        
        # Admin Login
        admin=Image.open(r"Images\Admin_login.png")
        admin=admin.resize((300,50),Image.ANTIALIAS)
        self.photoadmin=ImageTk.PhotoImage(admin) 

        b1=Button(bg_img,image=self.photoadmin,command=self.Admin_login_window,cursor="hand2",bd=2,relief=RIDGE,fg="white",bg="black",activeforeground="black",activebackground="black")
        b1.place(x=60,y=350,width=300,height=50)
        
        # Teacher Login
        teacher_lgn=Image.open(r"Images\Teacher_login.png")
        teacher_lgn=teacher_lgn.resize((300,50),Image.ANTIALIAS)
        self.phototeacher_lgn=ImageTk.PhotoImage(teacher_lgn) 

        b1=Button(bg_img,image=self.phototeacher_lgn,command=self.Teacher_login_window,cursor="hand2",bd=2,relief=RIDGE,fg="white",bg="black",activeforeground="black",activebackground="black")
        b1.place(x=60,y=410,width=300,height=50)
        
        # Exit
        exit_btn=Image.open(r"Images\Exit.png")
        exit_btn=exit_btn.resize((300,50),Image.ANTIALIAS)
        self.photoexit_btn=ImageTk.PhotoImage(exit_btn) 

        b1=Button(bg_img,command=self.iExit,image=self.photoexit_btn,cursor="hand2",bd=2,relief=RIDGE,fg="white",bg="black",activeforeground="black",activebackground="black")
        b1.place(x=60,y=470,width=300,height=50)
        

    # THis function is for open login window for teacher
    def Teacher_login_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Teacher_Login(self.new_window)
        
        

    # THis function is for open login window for admin
    def Admin_login_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Admin_Login(self.new_window)
        
        
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Do you want to exit",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
      

if __name__=="__main__":
    root=Tk()
    obj=Login_Page(root)
    root.mainloop()