from tkinter import * 
from PIL import Image, ImageTk, ImageDraw # pip install pillow
from datetime import *
import time
from math import *
import sqlite3
from tkinter import messagebox,ttk
import os


class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("                                                                                                                                                                                                                          Login System")
        self.root.geometry("1920x1080+0+0")
        self.root.config(bg="#021e2f")

        #================title
        
        #=================Background colors
        left_lbl = Label(self.root, bg="#08A3D2", bd=0)
        left_lbl.place(x=0, y=0, relheight=1, width=700)

        right_lbl = Label(self.root, bg="#031F3C", bd=0)
        right_lbl.place(x=700, y=0, relheight=1, relwidth=1)
        
        #=================Frames

        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=380,y=100,width=800,height=500)

        title = Label(login_frame,text="LOGIN HERE", font=("times new roman", 30, "bold"), bg="white", fg="#08A3D2").place(x=250,y=50)

        email = Label(login_frame,text="EMAIL ADDRESS", font=("times new roman", 18, "bold"), bg="white", fg="gray").place(x=250,y=150)
        self.txt_email = Entry(login_frame, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=250,y=180, width=350, height=35)

        pass_ = Label(login_frame,text="PASSWORD", font=("times new roman", 18, "bold"), bg="white", fg="gray").place(x=250,y=250)
        self.txt_pass_ = Entry(login_frame, font=("times new roman", 15), bg="lightgray")
        self.txt_pass_.place(x=250,y=280, width=350, height=35)

        btn_reg = Button(login_frame, text="Register New Account?", font=("times new roman", 14), bg="white", bd=0, fg="#B00857", cursor="hand2", command=self.register_window).place(x=250,y=320)
        btn_forget = Button(login_frame, text="Forget Password?", font=("times new roman", 14), bg="white", bd=0, fg="#B00857", cursor="hand2", command=self.forget_password_window).place(x=450,y=320)


        btn_login = Button(login_frame, text="Login", font=("times new roman", 20, "bold"), fg="white", bg="#B00857", cursor="hand2", command=self.login).place(x=250,y=380,width=180,height=40)











        #=================clock
        self.lbl = Label(self.root, text="\nClock",font=("Book Antiqua", 35, "bold"), compound=BOTTOM,fg="white",bg="#081923", bd=0)
        self.lbl.place(x=220, y=120, height=450, width=350)
        self.working()
#=========================Fucnctions===================================

    def reset(self):
        self.comb_quest.current(0)
        self.txt_new_password.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_pass_.delete(0,END)
        self.txt_email.delete(0,END)


    def forget_password(self):
        if self.comb_quest.get() == "Select" or self.txt_answer.get() == "" or self.txt_new_password.get() == "":
            messagebox.showerror("Error","All Fields Are Required", parent=self.root2)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("Select * from employee where email=? and question=? and answer=?", (self.txt_email.get(), self.comb_quest.get(), self.txt_answer.get()))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", " Please Select The Correct Security Question / Enter Answer", parent=self.root2)
                else:
                    cur.execute("update employee set password=? where email=?", (self.txt_new_password.get(), self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Your Passoword Has Been Reseted, Please Try Login With New Password", parent=self.root2)
                    self.reset()
                    self.root2.destroy()
            except Exception as es:
                messagebox.showerror("Error", f"Error Due To: {str(es)}", parent=self.root)




    def forget_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error", " Please Enter The Email Address To Reset Your Password", parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("Select * from employee where email=?", (self.txt_email.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", " Please Enter The Email Address To Reset Your Password", parent=self.root)
                else:
                    con.close()
                    self.root2 = Toplevel()
                    self.root2.title("                                    Forget Password")
                    self.root2.geometry("410x420+570+150")
                    self.root2.config(bg="white")
                    self.root2.focus_force() # it will focus toplevel window
                    self.root2.grab_set()    # it will grab the window until you close it

                    t = Label(self.root2, text="Forget Password", font=("times new roman", 25, "bold"), bg="white", fg="#B00857").place(x=0,y=15, relwidth=1)
                    
                    #=================Forget Password
                    question = Label(self.root2, text="Security Question", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=80,y=100)
                    self.comb_quest= ttk.Combobox(self.root2,font=("times new roman", 13), state="readonly", justify=CENTER)
                    self.comb_quest['values'] = ("Select", "Your First Pet Name", "Your Birth Place", "Your Best Friend Name")
                    self.comb_quest.place(x=80,y=130,width=250)
                    self.comb_quest.current(0)

                    answer = Label(self.root2, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=80,y=180)
                    self.txt_answer= Entry(self.root2,font=("times new roman", 15), bg="lightgray")
                    self.txt_answer.place(x=80,y=210,width=250)

                    new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=80,y=260)
                    self.txt_new_password= Entry(self.root2,font=("times new roman", 15), bg="lightgray")
                    self.txt_new_password.place(x=80,y=290,width=250)

                    btn_change_password = Button(self.root2, text="Change Password", bg="green", fg="white", font=("times new roman", 15, "bold"), command=self.forget_password).place(x=120, y=340)


            except Exception as es:
                messagebox.showerror("Error", f"Error Due To: {str(es)}", parent=self.root)
            
    
                        

    def register_window(self):
        self.root.destroy()
        os.system("python register.py")


    def login(self):
        if self.txt_email.get()=="" or self.txt_pass_.get()=="":
            messagebox.showerror("Error","All Fields Are Required", parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("Select * from employee where email=? and password=?", (self.txt_email.get(), self.txt_pass_.get()))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","INVALID USERNAME & PASSWORD", parent= self.root)
                else:
                    messagebox.showinfo("Success",f"WELCOME: {self.txt_email.get()}", parent= self.root)
                    self.root.destroy()
                    os.system("python dashboard.py")
                con.close()

            except Exception as es:
                messagebox.showerror("Error", f"Error Due To: {str(es)}", parent=self.root)
                


    def clock_image(self,hr,min_,sec_):
        clock = Image.new("RGB",(400,400),(8,25,35))   # bg white(255,255,255),  width, height = 400,400
        draw = ImageDraw.Draw(clock)

        #===========For Clock Image======
        bg = Image.open("images//c.png")
        bg= bg.resize((300,300), Image.ANTIALIAS)
        clock.paste(bg, (50,50))                            # x, y = 50,50
        #===========Formula To Rotate The Clock
        # angle_in_radians = angle_in_degrees * math.pi /180
        # line_length = 100
        # center_x = 250
        # center_y = 250
        # end_x = center_x + line_length * math.sin(angle_in_radians)
        # end_y = center_y - line_length * math.cos(angle_in_radians)
        
        #===========Hour Line Image======

        origin = 200,200
        #           x1, y1, x2, y2  
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill= "#DF005E",width=4)

        #===========Minute Line Image======
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill= "white",width=3)

        #===========Second Line Image======
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill= "yellow",width=2)
        draw.ellipse((195,195,210,210), fill="#1AD5D5") # for center in clock we used ellipse
        clock.save("images//clock_new.png")

    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
        hr = (h/12)*360   # we're converting it into angles
        min_ = (m/60)*360 # we're converting it into angles
        sec_ = (s/60)*360 # we're converting it into angles
        # print(h,m,s)
        # print(hr,min_,sec_)
        self.clock_image(hr,min_,sec_)
        self.img = ImageTk.PhotoImage(file="images//clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working) # refersing after 200 ms




root = Tk()
obj = Login_window(root)
root.mainloop()

