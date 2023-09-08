from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
# --------------------------
from Teacher_register import Teacher_Register
from Teacher_main import Teacher_Section
import os
import time

class Teacher_Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Teacher Login")
        self.root.geometry("340x450+520+270")
        self.root.resizable(False,False)
        self.root.focus_force()


        # variables 
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()

        self.bg=Image.open(r"images\Background_All.png")

        self.bg=self.bg.resize((1530,800),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(self.bg)

        lbl_bg=Label(self.root,image=self.photoimage)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame1= Frame(self.root,bg="black")
        frame1.place(x=0,y=0,width=340,height=450)
        

        img1=Image.open(r"Images\user1.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lb1img1 = Label(frame1,image=self.photoimage1,bg="black")
        lb1img1.place(x=130,y=5, width=100,height=100)
        

        get_str = Label(frame1,text="Login",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=140,y=100)

        #label1 
        username =lb1= Label(frame1,text="Email:",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=30,y=160)

        #entry1 
        self.txtuser=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtuser.place(x=33,y=190,width=270)


        #label2 
        pwd =lb1= Label(frame1,text="Password:",font=("times new roman",15,"bold"),fg="white",bg="black")
        pwd.place(x=30,y=230)

        #entry2 
        self.txtpwd=ttk.Entry(frame1,show="*",font=("times new roman",15,"bold"))
        self.txtpwd.place(x=33,y=260,width=270)
        
        # Login Button
        login_btn=Image.open(r"Images\Login.png")
        login_btn=login_btn.resize((120,35),Image.ANTIALIAS)
        self.photologin_btn=ImageTk.PhotoImage(login_btn) 

        b1=Button(frame1,image=self.photologin_btn,cursor="hand2",command=self.login,bd=2,relief=RIDGE,fg="white",bg="black",activeforeground="black",activebackground="black")
        b1.place(x=110,y=300,width=120,height=35)
        
        # Register Button
        registerbtn=Button(frame1,text="New User Register",command=self.reg,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=10,y=350,width=160)
        
        # Forget Password Button
        forgetbtn=Button(frame1,text="Forget Password ?",command=self.forget_pwd,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetbtn.place(x=10,y=380,width=160)
        
        # Delete Account Button
        forgetbtn=Button(frame1,text="Delete Account",command=self.delete_account,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetbtn.place(x=3,y=410,width=160)

    def login(self):
        if (self.txtuser.get()=="" or self.txtpwd.get()==""):
            messagebox.showerror("Error","All Field Required!",parent=self.root)
        elif(self.txtuser.get()=="admin" and self.txtpwd.get()=="admin"):
            messagebox.showinfo("Please write your email and password")
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="dipak0703@AG",database="face_recognition")
            mycursor = conn.cursor()
            mycursor.execute("select * from register where Email=%s and Password=%s",(
                self.txtuser.get(),
                self.txtpwd.get()
            ))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password!",parent=self.root)
            else:
                open_min=messagebox.askyesno("YesNo","Access only granted to Teachers",parent=self.root)
                if open_min>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Teacher_Section(self.new_window)
                    # root.withdraw()
                    # root.destroy()
                else:
                    if not open_min:
                        return
            conn.commit()
            conn.close()
            
            
# =====================Forget window=========================================
    def forget_pwd(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email ID to reset Password!",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="dipak0703@AG",database="face_recognition")
            mycursor = conn.cursor()
            query=("select * from register where Email=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("Error","Please Enter the Valid Email ID!")
            else:
                conn.close()
                self.root=Toplevel()
                self.root.title("Forget Password")
                self.root.geometry("400x400+610+170")
                l=Label(self.root,text="Forget Password",font=("times new roman",30,"bold"),fg="#002B53",bg="#fff")
                l.place(x=0,y=10,relwidth=1)
                # -------------------fields-------------------
                #label1 
                ssq =lb1= Label(self.root,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                ssq.place(x=70,y=80)

                #Combo Box1
                self.combo_security = ttk.Combobox(self.root,textvariable=self.var_ssq,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security["values"]=("Select","Your Birth Place","Your Bestfriend Name","Your Pet Name")
                self.combo_security.current(0)
                self.combo_security.place(x=70,y=110,width=270)


                #label2 
                sa =lb1= Label(self.root,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                sa.place(x=70,y=150)

                #entry2 
                self.txtpwd=ttk.Entry(self.root,textvariable=self.var_sa,font=("times new roman",15,"bold"))
                self.txtpwd.place(x=70,y=180,width=270)

                #label2 
                new_pwd =lb1= Label(self.root,text="New Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                new_pwd.place(x=70,y=220)

                #entry2 
                self.new_pwd=ttk.Entry(self.root,textvariable=self.var_pwd,show="*",font=("times new roman",15,"bold"))
                self.new_pwd.place(x=70,y=250,width=270)

                # Creating Button New Password
                loginbtn=Button(self.root,command=self.reset_pass,text="Reset Password",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
                loginbtn.place(x=70,y=300,width=270,height=35)


#=======================Reset Passowrd Function=============================
    def reset_pass(self):
        if self.var_ssq.get()=="Select":
            messagebox.showerror("Error","Select the Security Question!",parent=self.root)
        elif(self.var_sa.get()==""):
            messagebox.showerror("Error","Please Enter the Answer!",parent=self.root)
        elif(self.var_pwd.get()==""):
            messagebox.showerror("Error","Please Enter the New Password!",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="dipak0703@AG",database="face_recognition")
            mycursor = conn.cursor()
            query=("select * from register where Email=%s and Security_Q=%s and Security_A=%s")
            value=(self.txtuser.get(),self.var_ssq.get(),self.var_sa.get())
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the Correct Answer!",parent=self.root)
            else:
                query=("update register set Password=%s where Email=%s")
                value=(self.var_pwd.get(),self.txtuser.get())
                mycursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Successfully Your password has been rest, Please login with new Password!",parent=self.root)
                self.root.destroy()
                



   #==============================Delete Function=========================================
    def delete_account(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Email must Must be Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="dipak0703@AG",database="face_recognition")
                    mycursor = conn.cursor() 
                    sql="delete from register where Email=%s"
                    val=(self.txtuser.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)    


                
    # THis function is for open register window
    def reg(self):
        self.new_window=Toplevel(self.root)
        self.app=Teacher_Register(self.new_window)
  




if __name__ == "__main__":
    root=Tk()
    app=Teacher_Login(root)
    root.mainloop()