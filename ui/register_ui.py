import tkinter as tk
from tkinter import messagebox, simpledialog
from ui.common import show_frame
from server.user_managment import User




def register_user(type_of_user,username, password,login_frame):
    user_management = User()

    status = user_management.register_user(type_of_user, username, password)

    if status == 'true':

        messagebox.showinfo('Registration', 'Registration successful! Please log in.')
        show_frame(login_frame) 
    else:
       
        messagebox.showerror('Error', 'Username already exists')




def setUp_Register(login_frame, register_frame, user_dashboard_frame, admin_dashboard_frame):
    
   
    bg_image = tk.PhotoImage(file=r"C:\Users\iamaa\software\CSIA\dlms\images\bg.png")

   
    bg_label = tk.Label(register_frame, image=bg_image)
    bg_label.image = bg_image  
    bg_label.place(relwidth=1, relheight=1)  

    
    title = tk.Label(register_frame, text="Add a New User", font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
    title.place(x=0, y=0, relwidth=1, height=70)

   
    user_register_button = tk.Button(register_frame, text="Register User", font=("Arial", 14), command=lambda: register_user('non_admin', simpledialog.askstring("Register User", "Enter username:"),simpledialog.askstring("Register User", "Enter password:", show='*'),user_dashboard_frame))
    user_register_button.place(relx=0.5, rely=0.4, anchor='center')

    admin_register_button = tk.Button(register_frame, text="Register Admin", font=("Arial", 14), command=lambda: register_user('admin',  simpledialog.askstring("Register Admin", "Enter username:"),simpledialog.askstring("Register Admin", "Enter password:", show='*'),admin_dashboard_frame))
    admin_register_button.place(relx=0.5, rely=0.5, anchor='center')

    back_button = tk.Button(register_frame, text="Back to Login", font=("Arial", 14), command=lambda: show_frame(login_frame))
    back_button.place(relx=0.5, rely=0.6, anchor='center')
