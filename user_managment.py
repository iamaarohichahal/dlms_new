import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog
from werkzeug.security import generate_password_hash, check_password_hash



def register_user(username, password):
    """
    Registers a new user with a hashed password.
    """
    status = 'true'
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    hashed_password = generate_password_hash(password, method='sha256')
    try:
        # Insert new user into users table
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        #messagebox.showinfo('Registration', 'Registration successful! Please log in.')
        #show_frame(login_frame)  # Show login frame after successful registration
    except sqlite3.IntegrityError:
        status = 'false'
        #messagebox.showerror('Error', 'Username already exists')
    conn.close()
    return status