import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import Button, TOP, X
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the database
def init_db():
    """
    Initializes the SQLite databases and creates tables if they do not exist.
    """
    # Initialize the users database
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS users(
                   id INTEGER PRIMARY KEY,
                   username TEXT UNIQUE NOT NULL,
                   password TEXT NOT NULL)
                   ''')
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS books(
                   id INTEGER PRIMARY KEY,
                   title TEXT NOT NULL,
                   author TEXT NOT NULL,
                   year INTEGER NOT NULL,
                   isbn TEXT NOT NULL)
                   ''')
    conn.commit()
    conn.close()

    # Initialize the admin database
    conn = sqlite3.connect('admin.db')
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS admin(
                   id INTEGER PRIMARY KEY,
                   username TEXT UNIQUE NOT NULL,
                   password TEXT NOT NULL)
                   ''')
    conn.commit()
    conn.close()

def register_user(username, password):
    """
    Registers a new user with a hashed password.
    """
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    hashed_password = generate_password_hash(password, method='sha256')
    try:
        # Insert new user into users table
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        messagebox.showinfo('Registration', 'Registration successful! Please log in.')
        show_frame(login_frame)  # Show login frame after successful registration
    except sqlite3.IntegrityError:
        messagebox.showerror('Error', 'Username already exists')
    conn.close()

def register_admin(username, password):
    """
    Registers a new user with a hashed password.
    """
    conn = sqlite3.connect('admin.db')
    cursor = conn.cursor()
    hashed_password = generate_password_hash(password, method='sha256')
    try:
        # Insert new user into users table
        cursor.execute('INSERT INTO admin (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        messagebox.showinfo('Registration', 'Registration successful! Please log in.')
        show_frame(login_frame)  # Show login frame after successful registration
    except sqlite3.IntegrityError:
        messagebox.showerror('Error', 'Username already exists')
    conn.close()

def login_user(username, password):
    """
    Logs in a user by checking the username and password.
    """
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()

    # Verify password and show user dashboard if valid
    if user and check_password_hash(user[2], password):
        show_frame(user_dashboard_frame)
    else:
        messagebox.showerror('Error', 'Invalid username or password')

def login_admin(username, password):
    """
    Logs in an admin by checking the username and password.
    """
    conn = sqlite3.connect('admin.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM admin WHERE username = ?', (username,))
    admin = cursor.fetchone()
    conn.close()

    # Debugging prints
    print(f"Admin record: {admin}")
    print(f"Entered password: {password}")
    print(f"Stored hash: {admin[2] if admin else 'None'}")
    print(f"Password match: {check_password_hash(admin[2], password) if admin else 'None'}")

    # Verify password and show admin dashboard if valid
    if admin and check_password_hash(admin[2], password):
        show_frame(admin_dashboard_frame)
    else:
        messagebox.showerror('Error', 'Invalid username or password')



def add_book(title, author, year, isbn):
    """
    Adds a new book to the books table.
    """
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books (title, author, year, isbn) VALUES (?, ?, ?, ?)', 
                   (title, author, year, isbn))
    conn.commit()
    conn.close()
    messagebox.showinfo('Add Book', 'Book added successfully')

def browse_books():
    """
    Retrieves all books from the books table.
    """
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    conn.close()
    return books

def add_book_ui():
    """
    Creates the UI for adding a book.
    """
    for widget in add_book_frame.winfo_children():
        widget.destroy()  # Clear any existing widgets in the frame

    # Create and place UI elements for book details
    title_label = tk.Label(add_book_frame, text="Title", font=("Arial", 12))
    title_label.place(relx=0.5, rely=0.2, anchor='center')
    title_entry = tk.Entry(add_book_frame, font=("Arial", 12))
    title_entry.place(relx=0.5, rely=0.3, anchor='center')

    author_label = tk.Label(add_book_frame, text="Author", font=("Arial", 12))
    author_label.place(relx=0.5, rely=0.4, anchor='center')
    author_entry = tk.Entry(add_book_frame, font=("Arial", 12))
    author_entry.place(relx=0.5, rely=0.5, anchor='center')

    year_label = tk.Label(add_book_frame, text="Year", font=("Arial", 12))
    year_label.place(relx=0.5, rely=0.6, anchor='center')
    year_entry = tk.Entry(add_book_frame, font=("Arial", 12))
    year_entry.place(relx=0.5, rely=0.7, anchor='center')

    isbn_label = tk.Label(add_book_frame, text="ISBN", font=("Arial", 12))
    isbn_label.place(relx=0.5, rely=0.8, anchor='center')
    isbn_entry = tk.Entry(add_book_frame, font=("Arial", 12))
    isbn_entry.place(relx=0.5, rely=0.9, anchor='center')

    # Button to add the book
    add_button = tk.Button(add_book_frame, text="Add Book", font=("Arial", 14), command=lambda: add_book(
        title_entry.get(),
        author_entry.get(),
        year_entry.get(),
        isbn_entry.get()
    ))
    add_button.place(relx=0.5, rely=0.95, anchor='center')

    # Button to go back to the user dashboard
    back_button = tk.Button(add_book_frame, text="Back", font=("Arial", 14), command=lambda: show_frame(user_dashboard_frame))
    back_button.place(relx=0.5, rely=1.0, anchor='center')

    show_frame(add_book_frame)  # Show add book frame

def display_books(books):
    """
    Displays the list of books in the browse books frame.
    """
    for widget in browse_books_frame.winfo_children():
        widget.destroy()  # Clear any existing widgets in the frame
    
    # Create and place labels for each book
    for index, book in enumerate(books):
        book_label = tk.Label(browse_books_frame, text=f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}, ISBN: {book[4]}", font=("Arial", 12))
        book_label.place(relx=0.5, rely=0.2 + index*0.05, anchor='center')

    # Button to go back to the user dashboard
    back_button = tk.Button(browse_books_frame, text="Back", font=("Arial", 14), command=lambda: show_frame(user_dashboard_frame))
    back_button.place(relx=0.5, rely=0.9, anchor='center')

    show_frame(browse_books_frame)  # Show browse books frame

def show_frame(frame):
    """
    Raises the specified frame to the top.
    """
    frame.tkraise()

# Initialize the Tkinter application
app = tk.Tk()
app.title("Library Management System")
app.geometry("600x400")

# Initialize the database
init_db()

# Define frames with white background
login_frame = tk.Frame(app, bg='white')
register_frame = tk.Frame(app, bg='white')
user_dashboard_frame = tk.Frame(app, bg='white')
admin_dashboard_frame = tk.Frame(app, bg='white')
add_book_frame = tk.Frame(app, bg='white')
browse_books_frame = tk.Frame(app, bg='white')
profile_frame = tk.Frame(app, bg='white')
deposit_book_frame = tk.Frame(app, bg='white')
search_book_frame = tk.Frame(app, bg='white')
account_details_frame = tk.Frame(app, bg='white')
wishlist_frame = tk.Frame(app, bg='white')
loan_details_frame = tk.Frame(app, bg='white')
borrowing_history_frame = tk.Frame(app, bg='white')



# Place all frames to occupy the full window
for frame in (login_frame, register_frame, user_dashboard_frame, add_book_frame, browse_books_frame, profile_frame, deposit_book_frame, search_book_frame, 
              account_details_frame, loan_details_frame, borrowing_history_frame, wishlist_frame,admin_dashboard_frame):
    frame.place(relwidth=1, relheight=1)

# Login Frame
title = tk.Label(login_frame, text="Welcome to the Digital Library!", font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
title.place(x=0, y=0, relwidth=1, height=70)

# Button for User Login
user_login_button = tk.Button(login_frame, text="User Login", font=("Arial", 14), command=lambda: login_user(simpledialog.askstring("User Login", "Enter username:"), simpledialog.askstring("User Login", "Enter password:", show='*')))
user_login_button.place(relx=0.5, rely=0.4, anchor='center')

# Button for Admin Login
admin_login_button = tk.Button(login_frame, text="Admin Login", font=("Arial", 14), command=lambda: login_admin(simpledialog.askstring("Admin Login", "Enter username:"), simpledialog.askstring("Admin Login", "Enter password:", show='*')))
admin_login_button.place(relx=0.5, rely=0.5, anchor='center')

# Button to Register (Show Register Frame)
register_button = tk.Button(login_frame, text="Register", font=("Arial", 14), command=lambda: show_frame(register_frame))
register_button.place(relx=0.5, rely=0.6, anchor='center')
# Registration Frame
title = tk.Label(register_frame, text="Add a New User", font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
title.place(x=0, y=0, relwidth=1, height=70)

# Register button for User
user_register_button = tk.Button(register_frame, text="Register User", font=("Arial", 14), command=lambda: register_user(simpledialog.askstring("Register User", "Enter username:"), simpledialog.askstring("Register User", "Enter password:", show='*')))
user_register_button.place(relx=0.5, rely=0.4, anchor='center')

# Register button for Admin
admin_register_button = tk.Button(register_frame, text="Register Admin", font=("Arial", 14), command=lambda: register_admin(simpledialog.askstring("Register Admin", "Enter username:"), simpledialog.askstring("Register Admin", "Enter password:", show='*')))
admin_register_button.place(relx=0.5, rely=0.5, anchor='center')

# Back to Login button
back_button = tk.Button(register_frame, text="Back to Login", font=("Arial", 14), command=lambda: show_frame(login_frame))
back_button.place(relx=0.5, rely=0.6, anchor='center')

# admin Dashboard Frame
title = tk.Label(admin_dashboard_frame, text="Admin Dashboard", font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
title.place(x=0, y=0, relwidth=1, height=70)

# User Dashboard Frame
title = tk.Label(user_dashboard_frame, text="User Dashboard", font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
title.place(x=0, y=0, relwidth=1, height=70)

# Horizontal Menu Frame
DashboardMenu = tk.Frame(user_dashboard_frame, bd=2, relief="ridge", bg="white", height=50)
DashboardMenu.place(relx=0, rely=0.07, relwidth=1, height=50)  # Place under the title and make it horizontal

# Buttons for menu frame, aligned to the right
btn_browse_books = tk.Button(DashboardMenu, text="Browse Books", font=("times new roman", 12, "bold"), bg="white", width=15, command=lambda: display_books(browse_books()))
btn_browse_books.pack(side=tk.RIGHT, padx=5, pady=5)

btn_search_for_book = tk.Button(DashboardMenu, text="Search for Book", font=("times new roman", 12, "bold"), bg="white", width=15, command=lambda: show_frame(search_book_frame))
btn_search_for_book.pack(side=tk.RIGHT, padx=5, pady=5)

btn_deposit_book = tk.Button(DashboardMenu, text="Deposit Book", font=("times new roman", 12, "bold"), bg="white", width=15, command=lambda: show_frame(deposit_book_frame))
btn_deposit_book.pack(side=tk.RIGHT, padx=5, pady=5)

btn_my_profile = tk.Button(DashboardMenu, text="My Profile", font=("times new roman", 12, "bold"), bg="white", width=15, command=lambda: show_frame(profile_frame))
btn_my_profile.pack(side=tk.RIGHT, padx=5, pady=5)

# Button to go back to the user dashboard
back_button = tk.Button(profile_frame, text="Back", font=("Arial", 14), command=lambda: show_frame(user_dashboard_frame))
back_button.place(relx=0.5, rely=0.9, anchor='center')

# Deposit Book Frame
title = tk.Label(deposit_book_frame, text="Deposit Book", font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
title.place(x=0, y=0, relwidth=1, height=70)

# Button to go back to the user dashboard
back_button = tk.Button(deposit_book_frame, text="Back", font=("Arial", 14), command=lambda: show_frame(user_dashboard_frame))
back_button.place(relx=0.5, rely=0.9, anchor='center')

# Search Book Frame
title = tk.Label(search_book_frame, text="Search for Book", font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
title.place(x=0, y=0, relwidth=1, height=70)

# Button to go back to the user dashboard
back_button = tk.Button(search_book_frame, text="Back", font=("Arial", 14), command=lambda: show_frame(user_dashboard_frame))
back_button.place(relx=0.5, rely=0.9, anchor='center')

#browse book frame 
title = tk.Label(browse_books_frame, text="Browse Books", font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
title.place(x=0, y=0, relwidth=1, height=70)

# My Profile Frame
title = tk.Label(profile_frame, text="My Profile", font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
title.place(x=0, y=0, relwidth=1, height=70)

# Profile Buttons
account_details_button = tk.Button(profile_frame, text="Account Details", font=("Arial", 14), command=lambda: show_frame(account_details_frame))
account_details_button.place(relx=0.5, rely=0.3, anchor='center')

loan_details_button = tk.Button(profile_frame, text="Loan Details", font=("Arial", 14), command=lambda: show_frame(loan_details_frame))
loan_details_button.place(relx=0.5, rely=0.4, anchor='center')

borrowing_history_button = tk.Button(profile_frame, text="Borrowing History", font=("Arial", 14), command=lambda: show_frame(borrowing_history_frame))
borrowing_history_button.place(relx=0.5, rely=0.5, anchor='center')

wishlist_button = tk.Button(profile_frame, text="Wishlist", font=("Arial", 14), command=lambda: show_frame(wishlist_frame))
wishlist_button.place(relx=0.5, rely=0.6, anchor='center')

# Button to go back to the user dashboard
back_button = tk.Button(profile_frame, text="Back", font=("Arial", 14), command=lambda: show_frame(user_dashboard_frame))
back_button.place(relx=0.5, rely=0.9, anchor='center')

# Account Details Frame
title = tk.Label(account_details_frame, text="Account Details", font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
title.place(x=0, y=0, relwidth=1, height=70)

# Button to go back to the profile frame
back_button = tk.Button(account_details_frame, text="Back", font=("Arial", 14), command=lambda: show_frame(profile_frame))
back_button.place(relx=0.5, rely=0.9, anchor='center')

# Loan Details Frame
title = tk.Label(loan_details_frame, text="Loan Details", font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
title.place(x=0, y=0, relwidth=1, height=70)

# Button to go back to the profile frame
back_button = tk.Button(loan_details_frame, text="Back", font=("Arial", 14), command=lambda: show_frame(profile_frame))
back_button.place(relx=0.5, rely=0.9, anchor='center')

# Loan Details Frame
title = tk.Label(loan_details_frame, text="Loan Details", font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
title.place(x=0, y=0, relwidth=1, height=70)

# Button to go back to the profile frame
back_button = tk.Button(loan_details_frame, text="Back", font=("Arial", 14), command=lambda: show_frame(profile_frame))
back_button.place(relx=0.5, rely=0.9, anchor='center')

# Borrowing History Frame
title = tk.Label(borrowing_history_frame, text="Borrowing History", font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
title.place(x=0, y=0, relwidth=1, height=70)

# Button to go back to the profile frame
back_button = tk.Button(borrowing_history_frame, text="Back", font=("Arial", 14), command=lambda: show_frame(profile_frame))
back_button.place(relx=0.5, rely=0.9, anchor='center')

# Wishlist Frame
title = tk.Label(wishlist_frame, text="Wishlist", font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
title.place(x=0, y=0, relwidth=1, height=70)

# Button to go back to the profile frame
back_button = tk.Button(wishlist_frame, text="Back", font=("Arial", 14), command=lambda: show_frame(profile_frame))
back_button.place(relx=0.5, rely=0.9, anchor='center')


# Show Login Frame Initially
show_frame(login_frame)

# Run the Tkinter event loop
app.mainloop()