from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
from tkinter import messagebox


class Developer_Section:
    def __init__(self,root):
        self.root = root
        # print ("hello")  
        self.root.geometry("1530x800+0+0")
        self.root.title("Developer")
        self.root.resizable(False,False)
        self.root.focus_force()
        
        bg1=Image.open(r"Images\Developer_Main.png")
        bg1=bg1.resize((1515,790))
        self.photobg1=ImageTk.PhotoImage(bg1)
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=5,y=5,width=1515,height=790)
        

        # Exit
        exit_btn=Image.open(r"Images\Exit2.png")
        exit_btn=exit_btn.resize((100,50),Image.ANTIALIAS)
        self.photoexit_btn=ImageTk.PhotoImage(exit_btn) 

        b1=Button(bg_img,command=self.iExit,image=self.photoexit_btn,cursor="hand2",bd=0,relief=RIDGE,fg="white",bg="black",activeforeground="black",activebackground="black")
        b1.place(x=1430,y=750,width=100,height=50)


    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Developer","Do you want to exit",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
            
            
if __name__=="__main__":
    root=Tk()
    obj=Developer_Section(root)
    root.mainloop()