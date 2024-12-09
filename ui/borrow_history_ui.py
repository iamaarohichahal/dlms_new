import tkinter as tk
from tkinter import ttk, messagebox, END
import sqlite3
from ui.common import show_frame
from db_utils import Database






# -------------------------------------------
# Borrowing History Frame Setup
# -------------------------------------------
def setUp_borrowing_history(borrowing_history_frame,profile_frame):
    # Load the background image
    bg_image = tk.PhotoImage(file=r"C:\Users\iamaa\software\CSIA\dlms\images\bg.png")

    # Add the background image to the frame
    bg_label = tk.Label(borrowing_history_frame, image=bg_image)
    bg_label.image = bg_image  
    bg_label.place(relwidth=1, relheight=1)  # Make it cover the entire frame

    # Title label for Loan Details Frame
    borrowing_history_label = tk.Label(borrowing_history_frame, text="Borrowing History", font=("Arial", 20), bg="lightblue")
    borrowing_history_label.pack(pady=10)

    # Styling for the Treeview widget
    style = ttk.Style(borrowing_history_frame)
    style.theme_use('clam')
    style.configure('Treeview', font=("Arial", 14))
    style.map('Treeview', background=[('selected', '#1A8F2D')])

    # Creating the Treeview widget to display book data
    tree = ttk.Treeview(borrowing_history_frame, height=20)  

    # Defining columns for the Treeview
    tree['columns'] = ('ID', 'ISBN', 'Book Title', 'Book Author', 'Book Genre', 'Book Summary', 'Return Date')

    # Configuring columns
    tree.column('#0', width=0, stretch=tk.NO)
    tree.column('ID', anchor=tk.CENTER, width=50)
    tree.column('ISBN', anchor=tk.CENTER, width=250)
    tree.column('Book Title', anchor=tk.CENTER, width=200)
    tree.column('Book Author', anchor=tk.CENTER, width=200)
    tree.column('Book Genre', anchor=tk.CENTER, width=100)
    tree.column('Book Summary', anchor=tk.CENTER, width=200)
    tree.column('Return Date', anchor=tk.CENTER, width=250)

    # Defining headings
    tree.heading('ID', text='ID')
    tree.heading('ISBN', text='ISBN')
    tree.heading('Book Title', text='Book Title')
    tree.heading('Book Author', text='Book Author')
    tree.heading('Book Genre', text='Book Genre')
    tree.heading('Book Summary', text='Book Summary')
    tree.heading('Return Date', text='Return Date')

    # Place the Treeview widget in the center
    tree.place(relx=0.5, rely=0.5, anchor='center')  # Centered using relx, rely, and anchor

   

    back_button = tk.Button(borrowing_history_frame, text="Back", font=("Arial", 14), 
                            command=lambda: show_frame(profile_frame))
    back_button.place(relx=0.6, rely=0.9, anchor='center')

    