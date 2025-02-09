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

def view_overdue_books(overdue_books_tree, shared_data):
    """
    Updates the Treeview with overdue books for the current user.
    """
    user_id = shared_data.get_user_id()  # Get the user_id from shared_data

    # Assuming you have a method in Loan_management to get overdue books for a specific user
    loan_management = Loan_management()
    overdue_books = loan_management.get_overdue_books(user_id)

    # Clear existing items in the Treeview
    overdue_books_tree.delete(*overdue_books_tree.get_children())

    # Check if there are overdue books and insert them into the Treeview
    if overdue_books:
        for loan in overdue_books:
            # Assuming loan[0] is Book ID and loan[1] is Book Title, adjust according to your actual data structure
            overdue_books_tree.insert('', 'end', values=(loan[0], loan[1]))
    else:
        messagebox.showinfo("No Overdue Books", "You don't have any overdue books.")

# -------------------------------------------
# User Dashbaord Set Up
# -------------------------------------------
def setUp_user_dash(user_dashboard_frame, browse_books_frame, profile_frame, login_frame, shared_data):
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

    btn_logout = tk.Button(DashboardMenu, text="Logout", font=("Arial", 16, "bold"), bg="#4CAF50", fg="white", width=20, height=2, relief="solid", command=lambda: show_frame(login_frame))
    btn_logout.pack(side=tk.RIGHT, padx=5, pady=5)

    # Styling for the Treeview widget for overdue books
    style = ttk.Style(user_dashboard_frame)
    style.theme_use('clam')
    style.configure('Treeview', font=("Arial", 12))
    style.map('Treeview', background=[('selected', '#1A8F2D')])

    # Creating a title for the overdue books Treeview
    overdue_books_title = tk.Label(user_dashboard_frame, text="Overdue Books", font=("Arial", 14, "bold"), bg="white")
    overdue_books_title.place(x=630, y=120)

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
    overdue_books_tree.place(x=500, y=150)

    view_button = tk.Button(user_dashboard_frame, text="View", font=("Arial", 16, "bold"), bg="#4CAF50", fg="white", width=20, height=2, relief="solid", command=lambda: view_overdue_books(overdue_books_tree, shared_data))
    view_button.place(x=550, y=300)

    # Buttons for Browse Books and My Profile underneath the Treeview
    btn_browse_books_bottom = tk.Button(user_dashboard_frame, text="Browse Books", font=("Arial", 16, "bold"), bg="#4CAF50", fg="white", width=20, height=2, relief="solid", command=lambda: show_frame(browse_books_frame))
    btn_browse_books_bottom.place(x=250, y=500)

    btn_my_profile_bottom = tk.Button(user_dashboard_frame, text="My Profile", font=("Arial", 16, "bold"), bg="#4CAF50", fg="white", width=20, height=2, relief="solid", command=lambda: show_frame(profile_frame))
    btn_my_profile_bottom.place(x=850, y=500)
