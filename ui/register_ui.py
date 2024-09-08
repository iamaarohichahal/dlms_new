import tkinter as tk
import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash
from tkinter import messagebox, simpledialog
from ui.common import show_frame
from user_managment import register_user
from db_utils import DB_NAME



def local_register_user(username, password,login_frame):
    """
    Registers a new user locally by calling the register_user function.
    Displays appropriate message boxes based on registration status.
    """
    status = register_user(username, password)

    if status == 'true':
        # If registration is successful, show success message and navigate to login frame
        messagebox.showinfo('Registration', 'Registration successful! Please log in.')
        show_frame(login_frame)  # Show login frame after successful registration
    else:
        # If registration fails (e.g., username already exists), show error message
        messagebox.showerror('Error', 'Username already exists')

def register_admin(username, password, login_frame):
    """
    Registers a new admin by inserting username and hashed password into admin.db.
    Displays appropriate message boxes based on registration outcome.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    hashed_password = generate_password_hash(password, method='sha256')
    try:
        # Attempt to insert new admin credentials into the admin table
        cursor.execute('INSERT INTO admin (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        # On success, show success message and navigate to login frame
        messagebox.showinfo('Registration', 'Registration successful! Please log in.')
        show_frame(login_frame)  # Show login frame after successful registration
    except sqlite3.IntegrityError:
        # If insertion fails (e.g., username already exists), show error message
        messagebox.showerror('Error', 'Username already exists')
    conn.close()


# -------------------------------------------
# Registration Frame Setup
# -------------------------------------------
def setUp_Register(login_frame, register_frame, user_dashboard_frame, admin_dashboard_frame):
    
    # Title label for Registration Frame
    title = tk.Label(register_frame, text="Add a New User", font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
    title.place(x=0, y=0, relwidth=1, height=70)

    # Register button for User
    user_register_button = tk.Button(register_frame, text="Register User", font=("Arial", 14), 
                                    command=lambda: local_register_user(
                                        simpledialog.askstring("Register User", "Enter username:"),
                                        simpledialog.askstring("Register User", "Enter password:", show='*'),
                                        user_dashboard_frame
                                    ))
    user_register_button.place(relx=0.5, rely=0.4, anchor='center')

    # Register button for Admin
    admin_register_button = tk.Button(register_frame, text="Register Admin", font=("Arial", 14), 
                                    command=lambda: register_admin(
                                        simpledialog.askstring("Register Admin", "Enter username:"),
                                        simpledialog.askstring("Register Admin", "Enter password:", show='*'),
                                        admin_dashboard_frame
                                    ))
    admin_register_button.place(relx=0.5, rely=0.5, anchor='center')

    # Back to Login button
    back_button = tk.Button(register_frame, text="Back to Login", font=("Arial", 14), command=lambda: show_frame(login_frame))
    back_button.place(relx=0.5, rely=0.6, anchor='center')
