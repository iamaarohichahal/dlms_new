
import tkinter as tk
from tkinter import ttk
from db_utils import Database
from ui.common import show_frame
from ui.login_ui import setUp_Login
from ui.register_ui import setUp_Register
from ui.admin_dashboard_ui import setUp_admin_dash
from ui.user_dashboard_ui import setUp_user_dash
from ui.user_management_ui import setUp_user_management



# Create an instance of the Database class and initialize it
database = Database('user.db')
database.init_db()
database.close()


# -------------------------------------------
# Function Definitions
# -------------------------------------------





def add_book_ui():
    """
    Sets up the UI elements for adding a new book.
    Clears any existing widgets in the add_book_frame before setting up new ones.
    """
    # Clear existing widgets in the frame
    for widget in add_book_frame.winfo_children():
        widget.destroy()
    
    
    # Button to go back to the user dashboard
    back_button = tk.Button(add_book_frame, text="Back", font=("Arial", 14), command=lambda: show_frame(user_dashboard_frame))
    back_button.place(relx=0.5, rely=1.0, anchor='center')

    show_frame(add_book_frame)  # Show add book frame








# -------------------------------------------
# Application Initialization
# -------------------------------------------

# Initialize the Tkinter application
app = tk.Tk()
app.title("Library Management System")
app.geometry("600x400")


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


setUp_Login(login_frame, register_frame, user_dashboard_frame, admin_dashboard_frame)

setUp_Register(login_frame, register_frame, user_dashboard_frame, admin_dashboard_frame)

setUp_admin_dash(admin_dashboard_frame, user_management_frame,book_management_frame,loan_management_frame,login_frame)

setUp_user_dash(user_dashboard_frame, search_book_frame,deposit_book_frame,profile_frame,login_frame)

setUp_user_management(user_management_frame,admin_dashboard_frame)



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
