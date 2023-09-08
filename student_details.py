from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import tkinter

class student_details:
    def __init__(self, root):
        #Setting Up window form
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Student Details")
        self.root.resizable(False,False)
        self.root.focus_force()
        
    # ========Variable Declaration========
        self.var_dep=StringVar()
        self.var_std_id=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_name=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_age=StringVar()
        self.var_address=StringVar()
        self.var_email=StringVar()
        self.var_mob=StringVar()
        # self.var_std_id=StringVar()
        # self.var_teacher=StringVar()
        
        #Background Image
        bg1=Image.open(r"Images\Background_All.png")
        bg1=bg1.resize((1530,800))
        self.photobg1=ImageTk.PhotoImage(bg1)
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0,relwidth=1,relheight=1)

        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=62.4,y=258,width=1401.5,height=510)
        
        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("cambria",16,"bold"),fg="black")
        left_frame.place(x=0,y=10,width=700.5,height=480)

        # Current Course 
        current_course_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course",font=("cambria",14,"bold"),fg="black")
        current_course_frame.place(x=10,y=5,width=685,height=150)

        #label Department
        dep_label=Label(current_course_frame,text="DEPARTMENT",font=("cambria",14,"bold"),bg="white",fg="black")
        dep_label.place(x=5,y=15)

        #combo box 
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,width=15,font=("cambria",14),state="readonly")
        dep_combo["values"]=("Select Department","CSE","IT")
        dep_combo.current(0)
        dep_combo.place(x=140,y=15,width=200)
        

        # #Class Didvision
        # student_div_label = Label(current_course_frame,text="SECTION",font=("cambria",14,"bold"),bg="white",fg="black")
        # student_div_label.place(x=360,y=15)
        
        # #combo box 
        # div_combo=ttk.Combobox(current_course_frame,textvariable=self.var_div,width=13,font=("cambria",14),state="readonly")
        # div_combo["values"]=("Select","A","B","C","IT")
        # div_combo.current(0)
        # div_combo.place(x=465,y=15,width=200)
        #Student name
        student_id_label = Label(current_course_frame,text="Std-ID:",font=("cambria",14,"bold"),bg="white",fg="black")
        student_id_label.place(x=360,y=15)

        student_id_entry = ttk.Entry(current_course_frame,textvariable=self.var_std_id,width=25,font=("cambria",14))
        student_id_entry.place(x=465,y=15,width=200,height=25)

        #label Year
        year_label=Label(current_course_frame,text="YEAR",font=("cambria",14,"bold"),bg="white",fg="black")
        year_label.place(x=5,y=70)

        #combo box 
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,width=15,font=("cambria",14),state="readonly")
        year_combo["values"]=("Select Year","2023")
        year_combo.current(0)
        year_combo.place(x=140,y=70,width=200)

        #label Semester 
        year_label=Label(current_course_frame,text="SEMESTER",font=("cambria",14,"bold"),bg="white",fg="black")
        year_label.place(x=360,y=70)

        #combo box 
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,width=15,font=("cambria",14),state="readonly")
        year_combo["values"]=("Select Semester","Semester-4")
        year_combo.current(0)
        year_combo.place(x=465,y=70,width=200)

        #Class Student Information
        class_Student_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("cambria",16,"bold"),fg="black")
        class_Student_frame.place(x=10,y=160,width=685,height=230)
            
        #Student name
        student_name_label = Label(class_Student_frame,text="Name:",font=("cambria",14,"bold"),bg="white",fg="black")
        student_name_label.place(x=5,y=5)

        student_name_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=25,font=("cambria",14))
        student_name_entry.place(x=100,y=6,width=240,height=25)
        
        #Roll No
        student_roll_label = Label(class_Student_frame,text="Roll-No:",font=("cambria",14,"bold"),bg="white",fg="black")
        student_roll_label.place(x=345,y=5)

        student_roll_entry = ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=25,font=("cambria",14))
        student_roll_entry.place(x=430,y=6,width=240,height=25)

        #Gender
        student_gender_label = Label(class_Student_frame,text="Gender:",font=("cambria",14,"bold"),bg="white",fg="black")
        student_gender_label.place(x=5,y=45)

        #combo box 
        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,width=25,font=("cambria",14),state="readonly")
        gender_combo["values"]=("Select","Male","Female","Others")
        gender_combo.current(0)
        gender_combo.place(x=100,y=46,width=240,height=25)
        
        
        #Date of Birth
        student_dob_label = Label(class_Student_frame,text="DOB:",font=("cambria",14,"bold"),bg="white",fg="black")
        student_dob_label.place(x=345,y=45)

        student_dob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=25,font=("cambria",14))
        student_dob_entry.place(x=430,y=46,width=240,height=25)
        
        #Age
        student_age_label = Label(class_Student_frame,text="Age:",font=("cambria",14,"bold"),bg="white",fg="black")
        student_age_label.place(x=5,y=85)

        student_age_entry = ttk.Entry(class_Student_frame,textvariable=self.var_age,width=25,font=("cambria",14))
        student_age_entry.place(x=100,y=86,width=240,height=25)

        #Address
        student_address_label = Label(class_Student_frame,text="Address:",font=("cambria",14,"bold"),bg="white",fg="black")
        student_address_label.place(x=345,y=85)

        student_address_entry = ttk.Entry(class_Student_frame,textvariable=self.var_address,width=25,font=("cambria",14))
        student_address_entry.place(x=430,y=86,width=240,height=25)
        
        #Email
        student_email_label = Label(class_Student_frame,text="Email:",font=("cambria",14,"bold"),bg="white",fg="black")
        student_email_label.place(x=5,y=125)

        student_email_entry = ttk.Entry(class_Student_frame,textvariable=self.var_email,width=25,font=("cambria",14))
        student_email_entry.place(x=100,y=126,width=240,height=25)

        #Phone Number
        student_mob_label = Label(class_Student_frame,text="Contact:",font=("cambria",14,"bold"),bg="white",fg="black")
        student_mob_label.place(x=345,y=125)

        student_mob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_mob,width=25,font=("cambria",14))
        student_mob_entry.place(x=430,y=126,width=240,height=25)
        
        #Radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,text="Take Photo Sample",variable=self.var_radio1,value="Yes")
        radiobtn1.place(x=5,y=165)
        

        radiobtn1=ttk.Radiobutton(class_Student_frame,text="No Photo Sample",variable=self.var_radio1,value="No")
        radiobtn1.place(x=140,y=166)
        
        #Button Frame
        btn_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=10,y=390,width=685,height=60)


        # Save Button
        save_btn=Image.open(r"Images\Save.png")
        save_btn=save_btn.resize((100,40),Image.ANTIALIAS)
        self.photosave_btn=ImageTk.PhotoImage(save_btn) 

        b1=Button(btn_frame,image=self.photosave_btn,command=self.add_data,cursor="hand2",bd=2,relief=RIDGE,fg="white",bg="black",activeforeground="black",activebackground="black")
        b1.place(x=5,y=10,width=100,height=40)
        
        # Update Button
        update_btn=Image.open(r"Images\Update.png")
        update_btn=update_btn.resize((100,40),Image.ANTIALIAS)
        self.photoupdate_btn=ImageTk.PhotoImage(update_btn) 

        b2=Button(btn_frame,image=self.photoupdate_btn,command=self.update_data,cursor="hand2",bd=2,relief=RIDGE,fg="white",bg="black",activeforeground="black",activebackground="black")
        b2.place(x=115,y=10,width=100,height=40)
        
        # Delete Button
        delete_btn=Image.open(r"Images\Delete.png")
        delete_btn=delete_btn.resize((100,40),Image.ANTIALIAS)
        self.photodelete_btn=ImageTk.PhotoImage(delete_btn) 

        b3=Button(btn_frame,image=self.photodelete_btn,command=self.delete_data,cursor="hand2",bd=2,relief=RIDGE,fg="white",bg="black",activeforeground="black",activebackground="black")
        b3.place(x=225,y=10,width=100,height=40)
        
        # Reset Button
        reset_btn=Image.open(r"Images\Reset.png")
        reset_btn=reset_btn.resize((100,40),Image.ANTIALIAS)
        self.photoreset_btn=ImageTk.PhotoImage(reset_btn) 

        b4=Button(btn_frame,image=self.photoreset_btn,command=self.reset_data,cursor="hand2",bd=2,relief=RIDGE,fg="white",bg="black",activeforeground="black",activebackground="black")
        b4.place(x=335,y=10,width=100,height=40)
        
        # Take Pic Button
        take_pic_btn=Image.open(r"Images\Take_Pic.png")
        take_pic_btn=take_pic_btn.resize((100,40),Image.ANTIALIAS)
        self.phototake_pic_btn=ImageTk.PhotoImage(take_pic_btn) 

        b5=Button(btn_frame,image=self.phototake_pic_btn,command=self.generate_dataset,cursor="hand2",bd=2,relief=RIDGE,fg="white",bg="black",activeforeground="black",activebackground="black")
        b5.place(x=445,y=10,width=100,height=40)
        
        # Exit Button
        exit_new_btn=Image.open(r"Images\Exit1.png")
        exit_new_btn=exit_new_btn.resize((100,40),Image.ANTIALIAS)
        self.photoexit_new_btn=ImageTk.PhotoImage(exit_new_btn) 

        b6=Button(btn_frame,image=self.photoexit_new_btn,command=self.iExit,cursor="hand2",bd=2,relief=RIDGE,fg="white",bg="black",activeforeground="black",activebackground="black")
        b6.place(x=555,y=10,width=100,height=40)
        
#----------------------------------------------------------------------
        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("cambria",16,"bold"),fg="black")
        right_frame.place(x=701,y=10,width=700,height=480)

        #Searching System in Right Label Frame 
        search_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("cambria",16,"bold"),fg="black")
        search_frame.place(x=10,y=5,width=676,height=80)

        #Roll Number
        search_label = Label(search_frame,text="Search:",font=("cambria",14,"bold"),bg="white",fg="black")
        search_label.place(x=5,y=5)
        self.var_searchTX=StringVar()
        #combo box 
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_searchTX,width=12,font=("cambria",14),state="readonly")
        search_combo["values"]=("Select","Roll-No")
        search_combo.current(0)
        search_combo.place(x=85,y=6,width=140,height=25)

        self.var_search=StringVar()
        search_entry = ttk.Entry(search_frame,textvariable=self.var_search,width=12,font=("cambria",14))
        search_entry.place(x=240,y=6,width=140,height=25)

        # Search Button
        search_btn=Image.open(r"Images\Search.png")
        search_btn=search_btn.resize((130,40),Image.ANTIALIAS)
        self.photosearch_btn=ImageTk.PhotoImage(search_btn) 

        b7=Button(search_frame,image=self.photosearch_btn,command=self.search_data,cursor="hand2",bd=2,relief=RIDGE,fg="white",bg="black",activeforeground="black",activebackground="black")
        b7.place(x=390,y=2,width=130,height=40)
        
        # Show All Button
        show_all_btn=Image.open(r"Images\Show_All.png")
        show_all_btn=show_all_btn.resize((130,40),Image.ANTIALIAS)
        self.photoshow_all_btn=ImageTk.PhotoImage(show_all_btn) 

        b8=Button(search_frame,image=self.photoshow_all_btn,command=self.fetch_data,cursor="hand2",bd=2,relief=RIDGE,fg="white",bg="black",activeforeground="black",activebackground="black")
        b8.place(x=530,y=2,width=130,height=40)
        # # -----------------------------Table Frame-------------------------------------------------
        # #Table Frame 
        # #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=90,width=676,height=360)
        # scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.student_table = ttk.Treeview(table_frame,column=("Name","Dep","Roll-No","Year","Sem","ID","Age","Gender","DOB","Mob-No","Address","Email","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("Roll-No",text="Roll-No")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("ID",text="Student_ID")
        self.student_table.heading("Age",text="Age")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Mob-No",text="Contact")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Photo",text="PhotoSample")
        self.student_table["show"]="headings"


        # Set Width of Colums 
        self.student_table.column("Name",width=100)
        self.student_table.column("Dep",width=100)
        self.student_table.column("Roll-No",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("ID",width=100)
        self.student_table.column("Age",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Mob-No",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Photo",width=100)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        self.fetch_data()
        
#=======================CRUD operation functions========================================#
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_age.get()=="" or self.var_std_name.get()=="" or self.var_std_id.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_mob.get()=="" or self.var_address.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="dipak0703@AG",database="face_recognition")
                mycursor = conn.cursor()
                mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_std_name.get(),
                self.var_dep.get(),
                self.var_roll.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_std_id.get(),
                self.var_age.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_mob.get(),
                self.var_address.get(),
                self.var_email.get(),
                self.var_radio1.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","All Records are Saved!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    # ===========================Fetch data form database to table ================================

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="dipak0703@AG",database="face_recognition")
        mycursor = conn.cursor()

        mycursor.execute("select * from student")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #================================get cursor function=======================
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_std_name.set(data[0]),
        self.var_dep.set(data[1]),
        self.var_roll.set(data[2]),
        self.var_year.set(data[3]),
        self.var_semester.set(data[4]),
        self.var_std_id.set(data[5]),
        self.var_age.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_mob.set(data[9]),
        self.var_address.set(data[10]),
        self.var_email.set(data[11]),
        self.var_radio1.set(data[12])

    # ========================================Update Function==========================
    def update_data(self):
        
        if self.var_dep.get()=="Select Department" or self.var_age.get=="" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_std_name.get()=="" or self.var_std_id.get()=="Select" or self.var_roll.get()=="" or self.var_gender.get()=="Select" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_mob.get()=="" or self.var_address.get()=="":
            messagebox.showerror("Error","Please Fill.\nAll Fields are Required!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this Student Details!",parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="dipak0703@AG",database="face_recognition")
                    mycursor = conn.cursor()

                    mycursor.execute("Update student Set Student_Name=%s,Department=%s,Year=%s,Semester=%s,Student_ID=%s,Age=%s,Gender=%s,DOB=%s,Contact_No=%s,Address=%s,Email=%s,PhotoSample=%s where Roll_No=%s",( 
                                                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                                                        self.var_std_id.get(),
                                                                                                                                                                                                                        self.var_age.get(),
                                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                                        self.var_mob.get(),
                                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                                        self.var_roll.get()
                                                                                                                                                                                                                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
                
    #==============================Delete Function=========================================
    def delete_data(self):
        if self.var_roll.get()=="":
            messagebox.showerror("Error","Student Roll-No Must be Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="dipak0703@AG",database="face_recognition")
                    mycursor = conn.cursor() 
                    sql="delete from student where Roll_No=%s"
                    val=(self.var_roll.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)    
                
    # Reset Function 
    def reset_data(self):
        self.var_std_name.set(""),
        self.var_dep.set("Select Department"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_age.set(""),
        self.var_gender.set("Select"),
        self.var_dob.set(""),
        self.var_mob.set(""),
        self.var_address.set(""),
        self.var_roll.set(""),
        self.var_email.set(""),
        self.var_radio1.set("")


    # ===========================Search Data===================
    def search_data(self):
        if self.var_search.get()=="" or self.var_searchTX.get()=="Select":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="dipak0703@AG",database="face_recognition")
                my_cursor = conn.cursor()
                sql = "SELECT Student_Name,Department,Roll_No,Year,Semester,Student_ID,Age,Gender,DOB,Contact_No,Address,Email,PhotoSample FROM student where Roll_No='" +str(self.var_search.get()) + "'" 
                my_cursor.execute(sql)
                rows=my_cursor.fetchall()        
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    # ===========Function for Take Pic==========================
    def generate_dataset(self):
        if self.var_dep.get()=="select Department" or self.var_std_name.get()==""or self.var_roll.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="dipak0703@AG",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myResutl=my_cursor.fetchall()
                id=0
                sroll=self.var_roll.get()
                sname=self.var_std_name.get()
                for x in myResutl:
                    id+=1
                my_cursor.execute("update student set Department=%s,Age=%s,Year=%s,Semester=%s,Student_Name=%s,Student_ID=%s,Gender=%s,DOB=%s,Email=%s,Contact_No=%s,Address=%s,PhotoSample=%s where Roll_No=%s",(
                            self.var_dep.get(),
                            self.var_age.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get()==sname,
                            self.var_std_id.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_mob.get(),
                            self.var_address.get(),
                            self.var_radio1.get(),
                            self.var_roll.get()==sroll

                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                messagebox.showinfo(sname,parent=self.root)

                #========== Load data on frontal face from opencv=====
                face_classifier= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                 
                def face_cropped(img):
                    gry=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
                    faces=face_classifier.detectMultiScale(gry,1.3,5)

                    for(x,y,w,h)in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0

                while True:
                    ret,frame_my=cap.read()
                    if face_cropped(frame_my) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(frame_my),(500,500))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="StudentPhotoSample/"+str(sname)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2,(0,255,0),3)
                        cv2.imshow("Croped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Info","DataSet Completed!")

            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}", parent=self.root)




    # EXIT Function
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Do you want to exit",parent=self.root)
        if self.iExit>0:
            self.root.destroy()



if __name__ =="__main__":
    root=Tk()
    obj=student_details(root)
    root.mainloop() 