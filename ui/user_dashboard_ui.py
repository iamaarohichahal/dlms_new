import tkinter as tk
import time
from ui.common import show_frame
from tkinter import ttk
from tkinter import messagebox
from server.loan_management import Loan_management


def update_time(clock_label):
    current_time = time.strftime('%H:%M:%S %p')  # Format: Hour:Minute:Second AM/PM
    current_date = time.strftime('%Y-%m-%d')     # Format: Year-Month-Day
    clock_label.config(text=f"{current_date} {current_time}")
    clock_label.after(1000, update_time, clock_label)  # Update the clock every second



# -------------------------------------------
# User Dashbaord Set Up
# -------------------------------------------
def setUp_user_dash(user_dashboard_frame, browse_books_frame,profile_frame,login_frame):


    # Load the background image
    bg_image = tk.PhotoImage(file=r"C:\Users\iamaa\software\CSIA\dlms\images\bg.png")

    # Add the background image to the frame
    bg_label = tk.Label(user_dashboard_frame, image=bg_image)
    bg_label.image = bg_image  
    bg_label.place(relwidth=1, relheight=1)  # Make it cover the entire frame
    # Title label for User Dashboard Frame
    title = tk.Label(user_dashboard_frame, text="User Dashboard", font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
    title.place(x=0, y=0, relwidth=1, height=70)

    # Horizontal Menu Frame within User Dashboard
    DashboardMenu = tk.Frame(user_dashboard_frame, bd=2, relief="ridge", bg="white", height=50)
    DashboardMenu.place(relx=0, rely=0.07, relwidth=1, height=50)  # Place under the title and make it horizontal

    # Adding the clock label
    clock_label = tk.Label(DashboardMenu, font=("times new roman", 12, "bold"), bg="white")
    clock_label.pack(side=tk.LEFT, padx=10)  # Align it to the left

    # Start updating the clock
    update_time(clock_label)


    # Buttons for the horizontal menu, aligned to the right
    btn_browse_books = tk.Button(DashboardMenu, text="Browse Books", font=("times new roman", 12, "bold"), bg="white", width=15, command=lambda: show_frame(browse_books_frame))
    btn_browse_books.pack(side=tk.RIGHT, padx=5, pady=5)

    btn_my_profile = tk.Button(DashboardMenu, text="My Profile", font=("times new roman", 12, "bold"), bg="white", width=15, command=lambda: show_frame(profile_frame))
    btn_my_profile.pack(side=tk.RIGHT, padx=5, pady=5)

    btn_logout = tk.Button(DashboardMenu, text="Logout", font=("times new roman", 12, "bold"), bg="white", width=15, command=lambda: show_frame(login_frame))
    btn_logout.pack(side=tk.RIGHT, padx=5, pady=5)
        
    # Styling for the Treeview widget for overdue books
    style = ttk.Style(user_dashboard_frame)
    style.theme_use('clam')
    style.configure('Treeview', font=("Arial", 12))
    style.map('Treeview', background=[('selected', '#1A8F2D')])

    # Creating a title for the overdue books Treeview
    overdue_books_title = tk.Label(user_dashboard_frame, text="Overdue Books", font=("Arial", 14, "bold"), bg="white")
    overdue_books_title.place(x=20, y=120)

    # Creating the Treeview widget for overdue books
    overdue_books_tree = ttk.Treeview(user_dashboard_frame, height=5, columns=('Book ID', 'Book Name'))

    # Configuring columns
    overdue_books_tree.column('#0', width=0, stretch=tk.NO)
    overdue_books_tree.column('Book ID', anchor=tk.CENTER, width=100)
    overdue_books_tree.column('Book Name', anchor=tk.CENTER, width=300)

    # Defining headings
    overdue_books_tree.heading('Book ID', text='Book ID')
    overdue_books_tree.heading('Book Name', text='Book Name')

    # Placing the Treeview widget for overdue books
    overdue_books_tree.place(x=20, y=150)