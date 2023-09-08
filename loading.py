from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import time
from loginpage import Login_Page


class Startup:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("FRAMS")
        self.root.resizable(False,False)
        self.root.focus_force()

        bg1=Image.open(r"Images\Background_First.png")
        bg1=bg1.resize((1530,800))
        self.photobg1=ImageTk.PhotoImage(bg1)
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0,relwidth=1,relheight=1)
        
        st=Image.open(r"Images\Start.png")
        st=st.resize((550,70),Image.ANTIALIAS)
        self.photost=ImageTk.PhotoImage(st) 

        b1=Button(bg_img,command=self.runn,image=self.photost,cursor="hand2",bd=2,relief=RIDGE,fg="white",bg="black",activeforeground="black",activebackground="black")
        b1.place(x=440,y=600,width=550,height=70)
        
        
    def runn(self):
        root.withdraw()
        self.new_window=Toplevel(self.root)
        self.app=Login_Page(self.new_window)



if __name__ == "__main__":
    root=Tk()
    obj=Startup(root)
    root.mainloop()
    
    