import tkinter as tk
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk, Image



class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
       
        
        border = tk.LabelFrame(self, text='Login', bg='ivory', bd = 10, font=("Arial", 20))
        border.pack(fill="both", expand="yes", padx = 150, pady=150)
        
        L1 = tk.Label(border, text="Username", font=("Arial Bold", 15), bg='ivory')
        L1.place(x=50, y=20)
        T1 = tk.Entry(border, width = 30, bd = 5)
        T1.place(x=180, y=20)
        
        L2 = tk.Label(border, text="Password", font=("Arial Bold", 15), bg='ivory')
        L2.place(x=50, y=80)
        T2 = tk.Entry(border, width = 30, show='*', bd = 5)
        T2.place(x=180, y=80)
        
        def verify():
            try:
                with open("credential.txt", "r") as f:
                    info = f.readlines()
                    i  = 0
                    for e in info:
                        u, p =e.split(",")
                        if u.strip() == T1.get() and p.strip() == T2.get():
                            controller.show_frame(Userpage)
                            i = 1
                            break
                    if i==0:
                        messagebox.showinfo("Error", "Please provide correct username and password!!")
            except:
                messagebox.showinfo("Error", "Please provide correct username and password!!")
         
        B1 = tk.Button(border, text="User Login", font=("Arial", 15), command=verify)
        B1.place(x=320, y=115)
        
        def register():
            window = tk.Tk()
            window.resizable(0,0)
            window.configure(bg="deep sky blue")
            window.title("Register")
            l1 = tk.Label(window, text="Username:", font=("Arial",15), bg="deep sky blue")
            l1.place(x=10, y=10)
            t1 = tk.Entry(window, width=30, bd=5)
            t1.place(x = 200, y=10)
            
            l2 = tk.Label(window, text="Firstname:", font=("Arial",15), bg="deep sky blue")
            l2.place(x=10, y=60)
            t2 = tk.Entry(window, width=30, bd=5)
            t2.place(x = 200, y=60)

            l2 = tk.Label(window, text="Lastname:", font=("Arial",15), bg="deep sky blue")
            l2.place(x=10, y=110)
            t2 = tk.Entry(window, width=30, bd=5)
            t2.place(x = 200, y=110)
            
            l2 = tk.Label(window, text="Password:", font=("Arial",15), bg="deep sky blue")
            l2.place(x=10, y=160)
            t2 = tk.Entry(window, width=30, show="*", bd=5)
            t2.place(x = 200, y=160)
            
            l3 = tk.Label(window, text="Confirm Password:", font=("Arial",15), bg="deep sky blue")
            l3.place(x=10, y=210)
            t3 = tk.Entry(window, width=30, show="*", bd=5)
            t3.place(x = 200, y=210)
            
            def check():
                if t1.get()!="" or t2.get()!="" or t3.get()!="":
                    if t2.get()==t3.get():
                        with open("credential.txt", "a") as f:
                            f.write(t1.get()+","+t2.get()+"\n")
                            messagebox.showinfo("Welcome","You are registered successfully!!")
                    else:
                        messagebox.showinfo("Error","Your password didn't get match!!")
                else:
                    messagebox.showinfo("Error", "Please fill the complete field!!")
                    
            b1 = tk.Button(window, text="Register", font=("Arial",15), bg="#ffc22a", command=check)
            b1.place(x=300, y=350)
            
            window.geometry("670x420")
            window.mainloop()
            
        B2 = tk.Button(self, text="Register", bg = "orange", font=("Arial",15), command=register)
        B2.place(x=650, y=20)
        
        def admin():
            def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                border = tk.LabelFrame(self, text='Login', bg='ivory', bd = 10, font=("Arial", 20))
                border.pack(fill="both", expand="yes", padx = 150, pady=150)
        
                L1 = tk.Label(border, text="Username", font=("Arial Bold", 15), bg='ivory')
                L1.place(x=50, y=20)
                T1 = tk.Entry(border, width = 30, bd = 5)
                T1.place(x=180, y=20)
        
                L2 = tk.Label(border, text="Password", font=("Arial Bold", 15), bg='ivory')
                L2.place(x=50, y=80)
                T2 = tk.Entry(border, width = 30, show='*', bd = 5)
                T2.place(x=180, y=180)
        
        def verifyy():
            try:
                with open("credential.txt", "r") as f:
                    info = f.readlines()
                    i  = 0
                    for e in info:
                        u, p =e.split(",")
                        if u.strip() == T1.get() and p.strip() == T2.get():
                            controller.show_frame(Adminpage)
                            i = 1
                            break
                    if i==0:
                        messagebox.showinfo("Error", "Please provide correct username and password!!")
            except:
                messagebox.showinfo("Error", "Please provide correct username and password!!")
                
        B3 = tk.Button(self, text="Admin login", bg = "orange", font=("Arial",15), command=verifyy)
        B3.place(x=280, y=300)    
             
        
class Adminpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
         
        Button = tk.Button(self, text="Clothing", font=("Arial", 15), command=lambda: controller.show_frame(ThirdPage))
        Button.place(x=100, y=150)
        
        
        Button = tk.Button(self, text="Accessories ", font=("Arial", 15), command=lambda: controller.show_frame(ThirdPage))
        Button.place(x=100, y=200)
        
        
        Button = tk.Button(self, text="Kids wear", font=("Arial", 15), command=lambda: controller.show_frame(ThirdPage))
        Button.place(x=100, y=250)
        
        
        Button = tk.Button(self, text="Add Product", font=("Arial", 15), command=lambda: controller.show_frame(ThirdPage))
        Button.place(x=100, y=350)
        
        
        Button = tk.Button(self, text="Remove Product", font=("Arial", 15), command=lambda: controller.show_frame(ThirdPage))
        Button.place(x=100, y=400)
        
        
        Button = tk.Button(self, text="Next", font=("Arial", 15), command=lambda: controller.show_frame(ThirdPage))
        Button.place(x=400, y=450)

class Fourthpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.configure(bg='Tomato')
        Label = tk.Label(self, text="NIke shoes", bg = "white", font=("Arial Bold", 20))
        Label.place(x=30, y=100)
        
        Label = tk.Label(self, text="Available products", bg = "white", font=("Arial Bold", 20))
        Label.place(x=30, y=150)
        Label = tk.Label(self, text="Number of orders", bg = "white", font=("Arial Bold", 20))
        Label.place(x=30, y=200)
        
        Button = tk.Button(self, text="Log out", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
        Button.place(x=650, y=450)
        
        Button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(Adminpage))
        Button.place(x=100, y=450)
                

class Userpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        Button = tk.Button(self, text="Trending Products", font=("Arial", 15), command=lambda: controller.show_frame(Trending))
        Button.place(x=100, y=100)
        
         
        Button = tk.Button(self, text="Clothing", font=("Arial", 15), command=lambda: controller.show_frame(Clothing))
        Button.place(x=100, y=150)
        
        
        Button = tk.Button(self, text="Accessories ", font=("Arial", 15), command=lambda: controller.show_frame(Accessories))
        Button.place(x=100, y=200)
        
        
        Button = tk.Button(self, text="sports", font=("Arial", 15), command=lambda: controller.show_frame(sports))
        Button.place(x=100, y=300)
        
        
        Button = tk.Button(self, text="Electronics", font=("Arial", 15), command=lambda: controller.show_frame(Electronics))
        Button.place(x=100, y=350)
        
        
        Button = tk.Button(self, text="Next", font=("Arial", 15), command=lambda: controller.show_frame(FifthPage))
        Button.place(x=400, y=400)        

class Trending(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Label = tk.Label(self, text="Iphone 13", bg = "White", font=("Arial Bold", 20))
        Label.place(x=30, y=50)
        
        Label = tk.Label(self, text="Gucci Bag", bg = "White", font=("Arial Bold", 20))
        Label.place(x=30, y=100)
        
        Label = tk.Label(self, text="Samsung Tv", bg = "White", font=("Arial Bold", 20))
        Label.place(x=30, y=150)
        
        Label = tk.Label(self, text="NIke shoes", bg = "White", font=("Arial Bold", 20))
        Label.place(x=30, y=200)

        Button = tk.Button(self, text="back", font=("Arial", 15), command=lambda: controller.show_frame(Userpage))
        Button.place(x=400, y=400)
class Clothing(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Label = tk.Label(self, text="DENIM JEANS-99$", bg = "White", font=("Arial Bold", 20))
        Label.place(x=30, y=50)
        
        Label = tk.Label(self, text="UCB T-shirt-100$", bg = "White", font=("Arial Bold", 20))
        Label.place(x=30, y=100)
        
        Label = tk.Label(self, text="US polo shirt-200$", bg = "White", font=("Arial Bold", 20))
        Label.place(x=30, y=150)
        
        Label = tk.Label(self, text="Buffello jeans - 59$", bg = "White", font=("Arial Bold", 20))
        Label.place(x=30, y=200)

        Button = tk.Button(self, text="back", font=("Arial", 15), command=lambda: controller.show_frame(Userpage))
        Button.place(x=400, y=400)
class Accessories(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Label = tk.Label(self, text="Apple watch-199$", bg = "White", font=("Arial Bold", 20))
        Label.place(x=30, y=50)
        
        Label = tk.Label(self, text="Hat-39$", bg = "White", font=("Arial Bold", 20))
        Label.place(x=30, y=100)
        
        Label = tk.Label(self, text="ties-20$", bg = "White", font=("Arial Bold", 20))
        Label.place(x=30, y=150)
        
        Label = tk.Label(self, text="Ring - 30$", bg = "White", font=("Arial Bold", 20))
        Label.place(x=30, y=200)

        Button = tk.Button(self, text="back", font=("Arial", 15), command=lambda: controller.show_frame(Userpage))
        Button.place(x=400, y=400)
class sports(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Label = tk.Label(self, text="Vollyball - 25$", bg = "White", font=("Arial Bold", 20))
        Label.place(x=30, y=50)
        
        Label = tk.Label(self, text="Base ball - 30$", bg = "White", font=("Arial Bold", 20))
        Label.place(x=30, y=100)
        
        Label = tk.Label(self, text="Adidas shoes", bg = "White", font=("Arial Bold", 20))
        Label.place(x=30, y=150)
        
        Label = tk.Label(self, text="Nike shoes", bg = "White", font=("Arial Bold", 20))
        Label.place(x=30, y=200)

        Button = tk.Button(self, text="back", font=("Arial", 15), command=lambda: controller.show_frame(Userpage))
        Button.place(x=400, y=400)
class Electronics(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Label = tk.Label(self, text="Air Conditioner - 999$", bg = "White", font=("Arial Bold", 20))
        Label.place(x=30, y=50)
        
        Label = tk.Label(self, text="Black berry - 700$", bg = "White", font=("Arial Bold", 20))
        Label.place(x=30, y=100)
        
        Label = tk.Label(self, text="Xiami TV - 199$", bg = "White", font=("Arial Bold", 20))
        Label.place(x=30, y=150)
        
        Label = tk.Label(self, text="Laptop - 499$", bg = "White", font=("Arial Bold", 20))
        Label.place(x=30, y=200)

        Button = tk.Button(self, text="back", font=("Arial", 15), command=lambda: controller.show_frame(Userpage))
        Button.place(x=400, y=400)        
        
        
        
        
      
        
class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
    
        
        Label = tk.Label(self, text="--------------HAPPY SHOPPING----------------", bg = "white", font=("Arial Bold", 25))
        Label.place(x=40, y=150)
        
        Button = tk.Button(self, text="Log out", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
        Button.place(x=650, y=450)
        
        Button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(Adminpage))
        Button.place(x=100, y=450)
        
class FifthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
    
        
        Label = tk.Label(self, text="--------------HAPPY SHOPPING----------------", bg = "white", font=("Arial Bold", 25))
        Label.place(x=40, y=150)
        
        Button = tk.Button(self, text="Log out", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
        Button.place(x=650, y=450)
        
        Button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(Userpage))
        Button.place(x=100, y=450)        
        
        
class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        #creating a window
        window = tk.Frame(self)
        window.pack()
        
        window.grid_rowconfigure(0, minsize = 500)
        window.grid_columnconfigure(0, minsize = 800)
        
        self.frames = {}
        for F in (FirstPage, Userpage,Adminpage, Trending, ThirdPage, Fourthpage, Accessories, Clothing, Electronics, sports, FifthPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row = 0, column=0, sticky="nsew")
            
        self.show_frame(FirstPage)
        
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Online Shopping")
            
app = Application()
app.maxsize(800,500)
app.mainloop()
