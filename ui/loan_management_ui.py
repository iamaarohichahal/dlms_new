import tkinter as tk
from tkinter import ttk, END
from ui.common import show_frame
from server.loan_management import Loan_management


def add_loan_list_to_tree(loan_list_tree):
    loan_management = Loan_management()

    loans = loan_management.get_loans_2()
    loan_list_tree.delete(*loan_list_tree.get_children())
    for loan in loans:
        loan_list_tree.insert('', 'end', values=loan)


def setUp_loan_management(loan_management_frame, admin_dashboard_frame):
    
    # Load the background image
    bg_image = tk.PhotoImage(file=r"C:\Users\iamaa\software\CSIA\dlms\images\bg.png")
    
    # Add the background image to the frame
    bg_label = tk.Label(loan_management_frame, image=bg_image)
    bg_label.image = bg_image  # Keep a reference to avoid garbage collection
    bg_label.place(relwidth=1, relheight=1)  # Cover the entire frame
    
    # Header
    header_label = tk.Label(loan_management_frame, text="Loan Management",font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
    header_label.place(x=0, y=0, relwidth=1, height=70)


    
    # Styling for the Treeview widget
    style = ttk.Style(loan_management_frame)
    style.theme_use('clam')
    style.configure('Treeview', font=("Arial", 14))
    style.map('Treeview', background=[('selected', '#1A8F2D')])

    # Creating the Treeview widget to display loan records
    loan_list_tree = ttk.Treeview(loan_management_frame, height=20, columns=('Book ID', 'User ID', 'Borrow Date', 'Return Date', 'Status'))

    # Configuring columns
    loan_list_tree.column('#0', width=0, stretch=tk.NO)
    loan_list_tree.column('Book ID', anchor=tk.CENTER, width=100)
    loan_list_tree.column('User ID', anchor=tk.CENTER, width=100)
    loan_list_tree.column('Borrow Date', anchor=tk.CENTER, width=150)
    loan_list_tree.column('Return Date', anchor=tk.CENTER, width=150)
    loan_list_tree.column('Status', anchor=tk.CENTER, width=100)

    # Defining headings
    loan_list_tree.heading('Book ID', text='Book ID')
    loan_list_tree.heading('User ID', text='User ID')
    loan_list_tree.heading('Borrow Date', text='Borrow Date')
    loan_list_tree.heading('Return Date', text='Return Date')
    loan_list_tree.heading('Status', text='Status')

    add_loan_list_to_tree(loan_list_tree)

    # Placing the Treeview widget in the center of the frame
    loan_list_tree.place(relx=0.5, rely=0.4, anchor="center", width=900, height=500)
    
    # Back Button
    back_button = tk.Button(loan_management_frame, 
    text="Back", 
    font=("Arial", 14, "bold"), 
    bg="#1A8F2D",  # Green background
    fg="white",  # White text color
    width=20, 
    height=2,
    command=lambda: admin_dashboard_frame.tkraise())

    # Centering the button at the bottom
    back_button.place(relx=0.5, rely=0.9, anchor="center")