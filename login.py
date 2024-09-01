import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, simpledialog
from tkinter import Button, TOP, X
from werkzeug.security import generate_password_hash, check_password_hash
from db_utils import init_db
from user_managment import register_user

# -------------------------------------------
# Function Definitions
# -------------------------------------------

def local_register_user(username, password):
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

def register_admin(username, password):
    """
    Registers a new admin by inserting username and hashed password into admin.db.
    Displays appropriate message boxes based on registration outcome.
    """
    conn = sqlite3.connect('admin.db')
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

def login_user(username, password):
    """
    Logs in a user by verifying the username and password against the user.db database.
    Navigates to the user dashboard upon successful login.
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
    Logs in an admin by verifying the username and password against the admin.db database.
    Navigates to the admin dashboard upon successful login.
    """
    conn = sqlite3.connect('admin.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM admin WHERE username = ?', (username,))
    admin = cursor.fetchone()
    conn.close()

    # Debugging prints for development purposes
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
    Adds a new book to the books table in user.db.
    Displays a success message upon successful insertion.
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
    Retrieves all books from the books table in user.db.
    Returns a list of all books.
    """
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    conn.close()
    return books

def add_book_ui():
    """
    Sets up the UI elements for adding a new book.
    Clears any existing widgets in the add_book_frame before setting up new ones.
    """
    # Clear existing widgets in the frame
    for widget in add_book_frame.winfo_children():
        widget.destroy()
    
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
    Displays the list of books in the browse_books_frame.
    Clears any existing widgets before displaying the new list.
    """
    # Clear existing widgets in the frame
    for widget in browse_books_frame.winfo_children():
        widget.destroy()
    
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
    Brings the specified frame to the front, making it visible.
    """
    frame.tkraise()

def fetch_user_data():
    """
    Fetches user data from the library.db database.
    Returns a list of all users.
    """
    conn = sqlite3.connect('library.db')  # Replace with your actual database file
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")  # Replace 'users' with your actual table name
    rows = cursor.fetchall()
    conn.close()
    return rows

def edit_user(username):
    """
    Allows editing of a user's username and email through simple dialogs.
    Updates the user data and refreshes the user table display.
    """
    # Prompt for new username and email
    new_username = simpledialog.askstring("Edit User", f"Edit username for {username}:")
    new_email = simpledialog.askstring("Edit Email", f"Edit email for {username}:")
    # Update user data (in actual implementation, update database)
    for user in users:
        if user["username"] == username:
            user["username"] = new_username
            user["email"] = new_email
    populate_user_table()

def delete_user(username):
    """
    Deletes a user after confirmation.
    Updates the user data and refreshes the user table display.
    """
    # Confirm deletion
    if messagebox.askyesno("Delete User", f"Are you sure you want to delete {username}?"):
        # Delete user data (in actual implementation, delete from database)
        global users
        users = [user for user in users if user["username"] != username]
        populate_user_table()

def populate_user_table():
    """
    Populates the user management table with current user data.
    Clears existing entries before populating new ones.
    """
    # Clear existing rows
    for row in user_table.get_children():
        user_table.delete(row)
    # Insert user data into the table
    for user in users:
        user_table.insert("", "end", values=(user["username"], user["email"], "Edit", "Delete"))

# -------------------------------------------
# Application Initialization
# -------------------------------------------

# Initialize the Tkinter application
app = tk.Tk()
app.title("Library Management System")
app.geometry("600x400")

# Initialize the database
init_db()

# -------------------------------------------
# Frame Definitions
# -------------------------------------------

# Define all frames with white background
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
user_management_frame = tk.Frame(app, bg="white")
book_management_frame = tk.Frame(app, bg="white")
loan_management_frame = tk.Frame(app, bg="white")
reports_frame = tk.Frame(app, bg="white")
settings_frame = tk.Frame(app, bg="white")

# Place all frames to occupy the full window
for frame in (login_frame, register_frame, user_dashboard_frame, add_book_frame, browse_books_frame, profile_frame, deposit_book_frame, search_book_frame, 
              account_details_frame, loan_details_frame, borrowing_history_frame, wishlist_frame, admin_dashboard_frame, user_management_frame, 
              book_management_frame, loan_management_frame, reports_frame, settings_frame):
    frame.place(relwidth=1, relheight=1)

# -------------------------------------------
# Login Frame Setup
# -------------------------------------------

# Title label for Login Frame
title = tk.Label(login_frame, text="Welcome to the Digital Library!", font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
title.place(x=0, y=0, relwidth=1, height=70)

# Button for User Login
user_login_button = tk.Button(login_frame, text="User Login", font=("Arial", 14), 
                              command=lambda: login_user(
                                  simpledialog.askstring("User Login", "Enter username:"),
                                  simpledialog.askstring("User Login", "Enter password:", show='*')
                              ))
user_login_button.place(relx=0.5, rely=0.4, anchor='center')

# Button for Admin Login
admin_login_button = tk.Button(login_frame, text="Admin Login", font=("Arial", 14), 
                               command=lambda: login_admin(
                                   simpledialog.askstring("Admin Login", "Enter username:"),
                                   simpledialog.askstring("Admin Login", "Enter password:", show='*')
                               ))
admin_login_button.place(relx=0.5, rely=0.5, anchor='center')

# Button to Register (Show Register Frame)
register_button = tk.Button(login_frame, text="Register", font=("Arial", 14), command=lambda: show_frame(register_frame))
register_button.place(relx=0.5, rely=0.6, anchor='center')

# -------------------------------------------
# Registration Frame Setup
# -------------------------------------------

# Title label for Registration Frame
title = tk.Label(register_frame, text="Add a New User", font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
title.place(x=0, y=0, relwidth=1, height=70)

# Register button for User
user_register_button = tk.Button(register_frame, text="Register User", font=("Arial", 14), 
                                 command=lambda: local_register_user(
                                     simpledialog.askstring("Register User", "Enter username:"),
                                     simpledialog.askstring("Register User", "Enter password:", show='*')
                                 ))
user_register_button.place(relx=0.5, rely=0.4, anchor='center')

# Register button for Admin
admin_register_button = tk.Button(register_frame, text="Register Admin", font=("Arial", 14), 
                                  command=lambda: register_admin(
                                      simpledialog.askstring("Register Admin", "Enter username:"),
                                      simpledialog.askstring("Register Admin", "Enter password:", show='*')
                                  ))
admin_register_button.place(relx=0.5, rely=0.5, anchor='center')

# Back to Login button
back_button = tk.Button(register_frame, text="Back to Login", font=("Arial", 14), command=lambda: show_frame(login_frame))
back_button.place(relx=0.5, rely=0.6, anchor='center')

# -------------------------------------------
# Admin Dashboard Frame Setup
# -------------------------------------------

# Title label for Admin Dashboard Frame
title = tk.Label(admin_dashboard_frame, text="Admin Dashboard", font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
title.place(x=0, y=0, relwidth=1, height=70)

# Button to navigate to User Management
user_management_button = tk.Button(admin_dashboard_frame, text="Manage Users", font=("Arial", 14), command=lambda: show_frame(user_management_frame))
user_management_button.place(relx=0.5, rely=0.3, anchor='center')

# Button to navigate to Book Management
book_management_button = tk.Button(admin_dashboard_frame, text="Manage Books", font=("Arial", 14), command=lambda: show_frame(book_management_frame))
book_management_button.place(relx=0.5, rely=0.4, anchor='center')

# Button to navigate to Loan Management
loan_management_button = tk.Button(admin_dashboard_frame, text="Manage Loans", font=("Arial", 14), command=lambda: show_frame(loan_management_frame))
loan_management_button.place(relx=0.5, rely=0.5, anchor='center')

# Logout button for Admin
btn_logout_admin = tk.Button(admin_dashboard_frame, text="Logout", font=("times new roman", 12, "bold"), bg="white", width=15, command=lambda: show_frame(login_frame))
btn_logout_admin.place(relx=0.5, rely=0.6, anchor='center')

# -------------------------------------------
# User Management Frame Setup
# -------------------------------------------

# Title label for User Management Frame
user_management_label = tk.Label(user_management_frame, text="User Management", font=("Arial", 20), bg="lightgrey")
user_management_label.pack(pady=10)

# Labels and Entry fields for User Details
id_label = tk.Label(user_management_frame, font=("Arial", 14), text="User ID", bg="#69359c", fg="white")
id_label.place(x=20, y=50)

id_enter = tk.Entry(user_management_frame, font=("Arial", 14), bd=2, width=25, bg="#69359c", fg="white")
id_enter.place(x=150, y=50)

username_label = tk.Label(user_management_frame, font=("Arial", 14), text="Username", bg="#69359c", fg="white")
username_label.place(x=20, y=110)

username_enter = tk.Entry(user_management_frame, font=("Arial", 14), bd=2, width=25, bg="#69359c", fg="white")
username_enter.place(x=150, y=110)

password_label = tk.Label(user_management_frame, font=("Arial", 14), text="Password", bg="#69359c", fg="white")
password_label.place(x=20, y=170)

password_enter = tk.Entry(user_management_frame, font=("Arial", 14), bd=2, width=25, bg="#69359c", fg="white")
password_enter.place(x=150, y=170)

# Buttons for User Management Actions
add_user_button = tk.Button(user_management_frame, font=("Arial", 14), text="Add User")
add_user_button.place(x=20, y=300)

edit_user_button = tk.Button(user_management_frame, font=("Arial", 14), text="Edit User")
edit_user_button.place(x=20, y=400)

view_user_button = tk.Button(user_management_frame, font=("Arial", 14), text="View User")
view_user_button.place(x=20, y=500)

delete_user_button = tk.Button(user_management_frame, font=("Arial", 14), text="Delete User")
delete_user_button.place(x=20, y=600)

# Styling for the Treeview widget
style = ttk.Style(user_management_frame)
style.theme_use('clam')
style.configure('Treeview', font=("Arial", 14))
style.map('Treeview', background=[('selected', '#1A8F2D')])

# Creating the Treeview widget to display user data
tree = ttk.Treeview(user_management_frame, height=30)

# Defining columns for the Treeview
tree['columns'] = ('ID', 'Username', 'Password')

# Configuring columns
tree.column('#0', width=0, stretch=tk.NO)
tree.column('ID', anchor=tk.CENTER, width=150)
tree.column('Username', anchor=tk.CENTER, width=350)
tree.column('Password', anchor=tk.CENTER, width=350)

# Defining headings
tree.heading('ID', text='ID')
tree.heading('Username', text='Username')
tree.heading('Password', text='Password')

# Placing the Treeview widget
tree.place(x=450, y=50)

# Back button to return to Admin Dashboard
back_button = tk.Button(user_management_frame, text="Back", font=("Arial", 14), command=lambda: show_frame(admin_dashboard_frame))
back_button.place(relx=0.5, rely=0.9, anchor='center')

# -------------------------------------------
# Book Management Frame Setup
# -------------------------------------------

# Title label for Book Management Frame
book_management_label = tk.Label(book_management_frame, text="Book Management", font=("Arial", 20), bg="lightblue")
book_management_label.pack(pady=10)

# Labels and Entry fields for Book Details
isbn_label = tk.Label(book_management_frame, font=("Arial", 14), text= "ISBN ", bg="#69359c", fg="white")
isbn_label.place(x=20, y=50)

isbn_enter = tk.Entry(book_management_frame, font=("Arial", 14), bd=2, width=25, bg="#69359c", fg="white")
isbn_enter.place(x=150, y=50)

book_title_label = tk.Label(book_management_frame, font=("Arial", 14), text="Book Title", bg="#69359c", fg="white")
book_title_label.place(x=20, y=110)

book_title_enter = tk.Entry(book_management_frame, font=("Arial", 14), bd=2, width=25, bg="#69359c", fg="white")
book_title_enter.place(x=150, y=110)

book_author_label = tk.Label(book_management_frame, font=("Arial", 14), text="Book Author", bg="#69359c", fg="white")
book_author_label.place(x=20, y=170)

book_author_enter = tk.Entry(book_management_frame, font=("Arial", 14), bd=2, width=25, bg="#69359c", fg="white")
book_author_enter.place(x=150, y=170)

book_status_label = tk.Label(book_management_frame, font=("Arial", 14), text="Status", bg="#69359c", fg="white")
book_status_label.place(x=20, y=230)

book_status_enter = tk.Entry(book_management_frame, font=("Arial", 14), bd=2, width=25, bg="#69359c", fg="white")
book_status_enter.place(x=150, y=230)

# Buttons for User Management Actions
add_book_button = tk.Button(book_management_frame, font=("Arial", 14), text="Add Book")
add_book_button.place(x=20, y=340)

edit_book_button = tk.Button(book_management_frame, font=("Arial", 14), text="Edit Book")
edit_book_button.place(x=20, y=440)

view_book_button = tk.Button(book_management_frame, font=("Arial", 14), text="View Book")
view_book_button.place(x=20, y=540)

delete_book_button = tk.Button(book_management_frame, font=("Arial", 14), text="Delete Book")
delete_book_button.place(x=20, y=640)

# Styling for the Treeview widget
style = ttk.Style(book_management_frame)
style.theme_use('clam')
style.configure('Treeview', font=("Arial", 14))
style.map('Treeview', background=[('selected', '#1A8F2D')])

# Creating the Treeview widget to display user data
tree = ttk.Treeview(book_management_frame, height=30)

# Defining columns for the Treeview
tree['columns'] = ('ISBN', 'Book Title', 'Book Author', 'Status')

# Configuring columns
tree.column('#0', width=0, stretch=tk.NO)
tree.column('ISBN', anchor=tk.CENTER, width=150)
tree.column('Book Title', anchor=tk.CENTER, width=250)
tree.column('Book Author', anchor=tk.CENTER, width=250)
tree.column('Status', anchor=tk.CENTER, width=200)
# Defining headings
tree.heading('ISBN', text='ISBN')
tree.heading('Book Title', text='Book Title')
tree.heading('Book Author', text='Book Author')
tree.heading('Status', text='Status')

# Placing the Treeview widget
tree.place(x=450, y=50)

# Back button to return to Admin Dashboard
back_button = tk.Button(book_management_frame, text="Back", font=("Arial", 14), command=lambda: show_frame(admin_dashboard_frame))
back_button.place(relx=0.5, rely=0.9, anchor='center')

# -------------------------------------------
# Loan Management Frame Setup
# -------------------------------------------

# Title label for Loan Management Frame
loan_management_label = tk.Label(loan_management_frame, text="Loan Management", font=("Arial", 20), bg="lightgreen")
loan_management_label.pack(pady=10)

# Back button to return to Admin Dashboard
back_button = tk.Button(loan_management_frame, text="Back", font=("Arial", 14), command=lambda: show_frame(admin_dashboard_frame))
back_button.place(relx=0.5, rely=0.9, anchor='center')

# -------------------------------------------
# User Dashboard Frame Setup
# -------------------------------------------

# Title label for User Dashboard Frame
title = tk.Label(user_dashboard_frame, text="User Dashboard", font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
title.place(x=0, y=0, relwidth=1, height=70)

# Horizontal Menu Frame within User Dashboard
DashboardMenu = tk.Frame(user_dashboard_frame, bd=2, relief="ridge", bg="white", height=50)
DashboardMenu.place(relx=0, rely=0.07, relwidth=1, height=50)  # Place under the title and make it horizontal

# Buttons for the horizontal menu, aligned to the right
btn_browse_books = tk.Button(DashboardMenu, text="Browse Books", font=("times new roman", 12, "bold"), bg="white", width=15, command=lambda: display_books(browse_books()))
btn_browse_books.pack(side=tk.RIGHT, padx=5, pady=5)

btn_search_for_book = tk.Button(DashboardMenu, text="Search for Book", font=("times new roman", 12, "bold"), bg="white", width=15, command=lambda: show_frame(search_book_frame))
btn_search_for_book.pack(side=tk.RIGHT, padx=5, pady=5)

btn_deposit_book = tk.Button(DashboardMenu, text="Deposit Book", font=("times new roman", 12, "bold"), bg="white", width=15, command=lambda: show_frame(deposit_book_frame))
btn_deposit_book.pack(side=tk.RIGHT, padx=5, pady=5)

btn_my_profile = tk.Button(DashboardMenu, text="My Profile", font=("times new roman", 12, "bold"), bg="white", width=15, command=lambda: show_frame(profile_frame))
btn_my_profile.pack(side=tk.RIGHT, padx=5, pady=5)

btn_logout = tk.Button(DashboardMenu, text="Logout", font=("times new roman", 12, "bold"), bg="white", width=15, command=lambda: show_frame(login_frame))
btn_logout.pack(side=tk.RIGHT, padx=5, pady=5)

# -------------------------------------------
# Profile Frame Setup
# -------------------------------------------

# Title label for Profile Frame
title = tk.Label(profile_frame, text="My Profile", font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
title.place(x=0, y=0, relwidth=1, height=70)

# Profile management buttons
account_details_button = tk.Button(profile_frame, text="Account Details", font=("Arial", 14), command=lambda: show_frame(account_details_frame))
account_details_button.place(relx=0.5, rely=0.3, anchor='center')

loan_details_button = tk.Button(profile_frame, text="Loan Details", font=("Arial", 14), command=lambda: show_frame(loan_details_frame))
loan_details_button.place(relx=0.5, rely=0.4, anchor='center')

borrowing_history_button = tk.Button(profile_frame, text="Borrowing History", font=("Arial", 14), command=lambda: show_frame(borrowing_history_frame))
borrowing_history_button.place(relx=0.5, rely=0.5, anchor='center')

wishlist_button = tk.Button(profile_frame, text="Wishlist", font=("Arial", 14), command=lambda: show_frame(wishlist_frame))
wishlist_button.place(relx=0.5, rely=0.6, anchor='center')

# Back button to return to User Dashboard
back_button = tk.Button(profile_frame, text="Back", font=("Arial", 14), command=lambda: show_frame(user_dashboard_frame))
back_button.place(relx=0.5, rely=0.9, anchor='center')

# -------------------------------------------
# Other Frames Setup
# -------------------------------------------

# Function to create a standard frame with title and back button
def setup_frame(frame, title_text, back_command):
    title = tk.Label(frame, text=title_text, font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
    title.place(x=0, y=0, relwidth=1, height=70)
    back_button = tk.Button(frame, text="Back", font=("Arial", 14), command=back_command)
    back_button.place(relx=0.5, rely=0.9, anchor='center')

# Setting up Deposit Book Frame
setup_frame(deposit_book_frame, "Deposit Book", lambda: show_frame(user_dashboard_frame))

# Setting up Search Book Frame
setup_frame(search_book_frame, "Search for Book", lambda: show_frame(user_dashboard_frame))

# Setting up Browse Books Frame
setup_frame(browse_books_frame, "Browse Books", lambda: show_frame(user_dashboard_frame))

# Setting up Account Details Frame
setup_frame(account_details_frame, "Account Details", lambda: show_frame(profile_frame))

# Setting up Loan Details Frame
setup_frame(loan_details_frame, "Loan Details", lambda: show_frame(profile_frame))

# Setting up Borrowing History Frame
setup_frame(borrowing_history_frame, "Borrowing History", lambda: show_frame(profile_frame))

# Setting up Wishlist Frame
setup_frame(wishlist_frame, "Wishlist", lambda: show_frame(profile_frame))

# -------------------------------------------
# Initial Frame Display
# -------------------------------------------

# Show Login Frame Initially
show_frame(login_frame)

# Run the Tkinter event loop
app.mainloop()
