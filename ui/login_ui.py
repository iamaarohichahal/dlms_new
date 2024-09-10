import tkinter as tk
import sqlite3
from werkzeug.security import check_password_hash
from tkinter import messagebox, simpledialog, PhotoImage
from ui.common import show_frame
from db_utils import DB_NAME





def login_user(username, password, user_dashboard_frame):
    """
    Logs in a user by verifying the username and password against the user.db database.
    Navigates to the user dashboard upon successful login.
    """
    conn = sqlite3.connect('dlms.db')
    cursor = conn.cursor()
    
    # Fetch the user record from the database
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()

    # Verify password (comparing directly, assuming stored as plain text)
    if user and user[2] == password:  # user[2] should be the stored password
        show_frame(user_dashboard_frame)
    else:
        messagebox.showerror('Error', 'Invalid username or password')

        
def login_admin(username, password, admin_dashboard_frame):
    """
    Logs in an admin by verifying the username and password against the admin.db database.
    Navigates to the admin dashboard upon successful login.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Fetch the admin record from the database
    cursor.execute('SELECT * FROM admin WHERE username = ?', (username,))
    admin = cursor.fetchone()
    conn.close()

    # Verify password (comparing directly, assuming stored as plain text)
    if admin and admin[2] == password:  # admin[2] should be the stored password
        show_frame(admin_dashboard_frame)
    else:
        messagebox.showerror('Error', 'Invalid username or password')
# -------------------------------------------
# Login Frame Setup
# -------------------------------------------
def setUp_Login(login_frame, register_frame, user_dashboard_frame, admin_dashboard_frame):

    
    # Title label for Login Frame
    title = tk.Label(login_frame, text="Welcome to the Digital Library!", font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
    title.place(x=0, y=0, relwidth=1, height=70)

    # Button for User Login
    user_login_button = tk.Button(login_frame, text="User Login", font=("Arial", 14), 
                                command=lambda: login_user(
                                    simpledialog.askstring("User Login", "Enter username:"),
                                    simpledialog.askstring("User Login", "Enter password:", show='*'),
                                    user_dashboard_frame
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