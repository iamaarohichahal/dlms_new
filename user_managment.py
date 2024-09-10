import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog
from werkzeug.security import generate_password_hash, check_password_hash
from db_utils import DB_NAME



def register_user(username, password):
    """
    Registers a new user with a plain text password (not recommended for production).
    """
    status = 'true'
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    try:
        # Insert new user into users table with plain text password
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        # Optionally show success message and navigate to login frame (commented out for now)
        # messagebox.showinfo('Registration', 'Registration successful! Please log in.')
        # show_frame(login_frame)  # Show login frame after successful registration
    except sqlite3.IntegrityError:
        status = 'false'
        # Optionally show error message (commented out for now)
        # messagebox.showerror('Error', 'Username already exists')
    
    conn.close()
    return status
