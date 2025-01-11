import tkinter as tk
import sqlite3
from werkzeug.security import check_password_hash
from tkinter import messagebox, simpledialog, PhotoImage
from ui.common import show_frame
from db_utils import DB_NAME
from server.login import Login


def login_user(username, password, user_dashboard_frame, shared_data):
    login = Login()
    if login.validate_user('non_admin', username,password) ==  True:

        print(f"User {username} logged in with User ID: {username}")
        
        shared_data.set_user_id(username)
        
        show_frame(user_dashboard_frame)
    else:
        messagebox.showerror('Error', 'Invalid username or password')


        
def login_admin(username, password, admin_dashboard_frame):
    login = Login()
    if login.validate_user('admin',username, password) == True:
        show_frame(admin_dashboard_frame)
    else:
        messagebox.showerror('Error', 'Invalid username or password')

        
# -------------------------------------------
# Login Frame Setup
# -------------------------------------------
def setUp_Login(login_frame, register_frame, user_dashboard_frame, admin_dashboard_frame, shared_data):

    
    # Title label for Login Frame
    title = tk.Label(login_frame, text="Library Management System", font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
    title.place(x=0, y=0, relwidth=1, height=70)

    # Button for User Login
    user_login_button = tk.Button(login_frame, text="User Login", font=("Arial", 14), 
                                command=lambda: login_user(
                                    simpledialog.askstring("User Login", "Enter username:"),
                                    simpledialog.askstring("User Login", "Enter password:", show='*'),
                                    user_dashboard_frame,
                                    shared_data
                                ))
    user_login_button.place(relx=0.5, rely=0.4, anchor='center')

    # Button for Admin Login
    admin_login_button = tk.Button(login_frame, text="Admin Login", font=("Arial", 14), 
                                command=lambda: login_admin(
                                    simpledialog.askstring("Admin Login", "Enter username:"),
                                    simpledialog.askstring("Admin Login", "Enter password:", show='*'),
                                    admin_dashboard_frame
                                ))
    admin_login_button.place(relx=0.5, rely=0.5, anchor='center')

    # Button to Register (Show Register Frame)
    register_button = tk.Button(login_frame, text="Register", font=("Arial", 14), command=lambda: show_frame(register_frame))
    register_button.place(relx=0.5, rely=0.6, anchor='center')