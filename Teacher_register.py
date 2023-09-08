from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class Teacher_Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1530x800+0+0")
        self.root.resizable(False,False)
        self.root.focus_force()

        # ============ Variables =================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_cnum=StringVar()
        self.var_email=StringVar()
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()
        self.var_cpwd=StringVar()
        self.var_check=IntVar()
        self.var_admin=StringVar()

        self.bg=ImageTk.PhotoImage(file=r"Images\Background_ALL.png")
        
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)

        frame= Frame(self.root,bg="white")  ###white
        frame.place(x=320,y=240,width=900,height=500)
        

        get_str = Label(frame,text="Registration",font=("times new roman",30,"bold"),fg="black",bg="white")
        get_str.place(x=350,y=20)

        #label1 
        fname = Label(frame,text="First Name:",font=("times new roman",15,"bold"),fg="black",bg="white")
        fname.place(x=100,y=100)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.txtuser.place(x=103,y=125,width=270)


        #label2 
        lname = Label(frame,text="Last Name:",font=("times new roman",15,"bold"),fg="black",bg="white")
        lname.place(x=100,y=170)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=103,y=195,width=270)

        # ==================== section 2 -------- 2nd Columan===================

        #label1 
        cnum = Label(frame,text="Contact No:",font=("times new roman",15,"bold"),fg="black",bg="white")
        cnum.place(x=530,y=100)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_cnum,font=("times new roman",15,"bold"))
        self.txtuser.place(x=533,y=125,width=270)


        #label2 
        email =lb1= Label(frame,text="Email:",font=("times new roman",15,"bold"),fg="black",bg="white")
        email.place(x=530,y=170)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=533,y=195,width=270)

        # ========================= Section 3 --- 1 Columan=================

        #label1 
        ssq =lb1= Label(frame,text="Select Security Question:",font=("times new roman",15,"bold"),fg="black",bg="white")
        ssq.place(x=100,y=250)

        #Combo Box1
        self.combo_security = ttk.Combobox(frame,textvariable=self.var_ssq,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security["values"]=("Select","Your Birth Place","Your Bestfriend Name","Your Pet Name")
        self.combo_security.current(0)
        self.combo_security.place(x=103,y=275,width=270)


        #label2 
        sa = Label(frame,text="Security Answer:",font=("times new roman",15,"bold"),fg="black",bg="white")
        sa.place(x=100,y=320)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_sa,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=103,y=345,width=270)

        # ========================= Section 4-----Column 2=============================

        #label1 
        pwd = Label(frame,text="Password:",font=("times new roman",15,"bold"),fg="black",bg="white")
        pwd.place(x=530,y=250)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_pwd,show="*",font=("times new roman",15,"bold"))
        self.txtuser.place(x=533,y=275,width=270)


        #label2 
        cpwd = Label(frame,text="Confirm Password:",font=("times new roman",15,"bold"),fg="black",bg="white")
        cpwd.place(x=530,y=320)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_cpwd,show="*",font=("times new roman",15,"bold"))
        self.txtpwd.place(x=533,y=345,width=270)

        adminVerify = Label(frame,text="Verification Code:",font=("times new roman",15,"bold"),fg="black",bg="white")
        adminVerify.place(x=100,y=390)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_admin,show="*",font=("times new roman",15,"bold"))
        self.txtpwd.place(x=270,y=390,width=270)

        # Checkbutton
        checkbtn = Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions",font=("times new roman",13,"bold"),fg="black",bg="white")
        checkbtn.place(x=100,y=420,width=270)


        # Creating Button Register
        rgtbtn=Image.open(r"Images\Register.png")
        rgtbtn=rgtbtn.resize((300,40),Image.ANTIALIAS)
        self.photorgtbtn=ImageTk.PhotoImage(rgtbtn) 

        b1=Button(frame,image=self.photorgtbtn,cursor="hand2",command=self.reg,bd=2,relief=RIDGE,fg="white",bg="black",activeforeground="black",activebackground="black")
        b1.place(x=60,y=450,width=300,height=40)
        
        # Goto Login page button
        lgnbtn=Image.open(r"Images\Login.png")
        lgnbtn=lgnbtn.resize((300,40),Image.ANTIALIAS)
        self.photolgnbtn=ImageTk.PhotoImage(lgnbtn) 

        b1=Button(frame,image=self.photolgnbtn,cursor="hand2",command=self.return_login,bd=2,relief=RIDGE,fg="white",bg="black",activeforeground="black",activebackground="black")
        b1.place(x=530,y=450,width=300,height=40)
        
        # Creating Button Login
    def return_login(self):
        self.root.destroy()


    def reg(self):
        
            if (self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_cnum.get()=="" or self.var_email.get()=="" or self.var_ssq.get()=="Select" or self.var_sa.get()=="" or self.var_pwd.get()=="" or self.var_cpwd.get()==""):
                messagebox.showerror("Error","All Field Required!",parent=self.root)
            elif(self.var_pwd.get() != self.var_cpwd.get()):
                messagebox.showerror("Error","Please Enter Password & Confirm Password are Same!",parent=self.root)
            elif(self.var_check.get()==0):
                messagebox.showerror("Error","Please Check the Agree Terms and Conditons!",parent=self.root)
            else:
                try:
                    conn = mysql.connector.connect(host="localhost",username="root",password="dipak0703@AG",database="face_recognition")
                    mycursor = conn.cursor()
                    query=("select * from register where Email=%s")
                    value=(self.var_email.get(),)
                    mycursor.execute(query,value)
                    row=mycursor.fetchone()
                    if row!=None:
                        messagebox.showerror("Error","User already exist,please try another email",parent=self.root)
                    else:
                        veri=self.var_admin.get()
                        if veri=="SIT@1999":

                            mycursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                            self.var_fname.get(),
                            self.var_lname.get(),
                            self.var_cnum.get(),
                            self.var_email.get(),
                            self.var_ssq.get(),
                            self.var_sa.get(),
                            self.var_pwd.get()
                            ))
                            messagebox.showinfo("Success","Successfully Registerd!",parent=self.root)
                        else:
                            messagebox.showerror("Error","Admin not verified! Wrong password",parent=self.root)

                        conn.commit()
                        conn.close()
                        
                except Exception as es:
                    messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)





if __name__ == "__main__":
    root=Tk()
    app=Teacher_Register(root)
    root.mainloop()