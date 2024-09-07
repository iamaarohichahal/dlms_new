import tkinter as tk
from tkinter import ttk, messagebox 
from ui.common import show_frame



# -------------------------------------------
# Book Management Frame Setup
# -------------------------------------------
def setUp_book_management(book_management_frame,admin_dashboard_frame):
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