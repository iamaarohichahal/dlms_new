import tkinter as tk
from tkinter import ttk, messagebox 
from ui.common import show_frame
from db_utils import Database

def insert_books_treeview(isbn_enter, book_title_enter, book_author_enter, book_genre_enter, book_summary_enter, book_status_enter, tree):
    database = Database()  # Assuming the books are in 'user.db'
    
    # Retrieve values from the entry fields and combo box
    isbn = isbn_enter.get()
    book_title = book_title_enter.get()
    book_author = book_author_enter.get()
    book_genre = book_genre_enter.get()
    book_summary = book_summary_enter.get()
    book_status = book_status_enter.get()  # This gets the selected value from the combo box

    # Check if any field is empty
    if not (isbn and book_title and book_author and book_genre and book_summary and book_status):
        messagebox.showerror('Error', 'Please enter all the fields')
    else:
        # Insert the new book into the database
        database.insert_book(isbn, book_title, book_author, book_genre, book_summary, book_status)

        # Refresh the tree view with updated data
        add_books_to_tree(tree)

        # Display success message
        messagebox.showinfo('Success', "Book has been inserted successfully")



# Function to refresh the tree view with books
def add_books_to_tree(tree):
    # Clear the existing rows
    for row in tree.get_children():
        tree.delete(row)
    
    database = Database()
    books = database.fetch_books()
    
    # Insert books into the treeview
    for book in books:
        tree.insert("", "end", values=book)

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

    isbn_enter = tk.Entry(book_management_frame, font=("Arial", 14), bd=2, width=20, bg="#69359c", fg="white")
    isbn_enter.place(x=150, y=50)

    book_title_label = tk.Label(book_management_frame, font=("Arial", 14), text="Book Title", bg="#69359c", fg="white")
    book_title_label.place(x=20, y=110)

    book_title_enter = tk.Entry(book_management_frame, font=("Arial", 14), bd=2, width=20, bg="#69359c", fg="white")
    book_title_enter.place(x=150, y=110)

    book_author_label = tk.Label(book_management_frame, font=("Arial", 14), text="Book Author", bg="#69359c", fg="white")
    book_author_label.place(x=20, y=170)

    book_author_enter = tk.Entry(book_management_frame, font=("Arial", 14), bd=2, width=20, bg="#69359c", fg="white")
    book_author_enter.place(x=150, y=170)

    book_genre_label = tk.Label(book_management_frame, font=("Arial", 14), text="Genre", bg="#69359c", fg="white")
    book_genre_label.place(x=20, y=230)

    book_genre_enter = tk.Entry(book_management_frame, font=("Arial", 14), bd=2, width=20, bg="#69359c", fg="white")
    book_genre_enter.place(x=150, y=230)

    book_summary_label = tk.Label(book_management_frame, font=("Arial", 14), text="Summary", bg="#69359c", fg="white")
    book_summary_label.place(x=20, y=290)

    book_status_enter = tk.Entry(book_management_frame, font=("Arial", 14), bd=2, width=20, bg="#69359c", fg="white")
    book_status_enter.place(x=150, y=290)

    book_status_label = tk.Label(book_management_frame, font=("Arial", 14), text="Status", bg="#69359c", fg="white")
    book_status_label.place(x=20, y=350)

    book_status_enter = ttk.Combobox(book_management_frame, font=("Arial", 14), width=18)
    book_status_enter['values'] = ("Available", "Borrowed")  # Set the options in the drop-down
    book_status_enter.place(x=150, y=350)


    # Buttons for User Management Actions
    add_book_button = tk.Button(book_management_frame, font=("Arial", 14), text="Add Book")
    add_book_button.place(x=20, y=400)

    edit_book_button = tk.Button(book_management_frame, font=("Arial", 14), text="Edit Book")
    edit_book_button.place(x=20, y=450)

    view_book_button = tk.Button(book_management_frame, font=("Arial", 14), text="View Book")
    view_book_button.place(x=20, y=500)

    delete_book_button = tk.Button(book_management_frame, font=("Arial", 14), text="Delete Book")
    delete_book_button.place(x=20, y=550)

    # Styling for the Treeview widget
    style = ttk.Style(book_management_frame)
    style.theme_use('clam')
    style.configure('Treeview', font=("Arial", 14))
    style.map('Treeview', background=[('selected', '#1A8F2D')])

    # Creating the Treeview widget to display user data
    tree = ttk.Treeview(book_management_frame, height=30)

    # Defining columns for the Treeview
    tree['columns'] = ('ISBN', 'Book Title', 'Book Author', 'Book Genre', 'Book Summary', 'Status')


    # Configuring columns
    tree.column('#0', width=0, stretch=tk.NO)
    tree.column('ISBN', anchor=tk.CENTER, width=100)
    tree.column('Book Title', anchor=tk.CENTER, width=200)
    tree.column('Book Author', anchor=tk.CENTER, width=200)
    tree.column('Book Genre', anchor=tk.CENTER, width=100)
    tree.column('Book Summary', anchor=tk.CENTER, width=200)
    tree.column('Status', anchor=tk.CENTER, width=100)

    # Defining headings
    tree.heading('ISBN', text='ISBN')
    tree.heading('Book Title', text='Book Title')
    tree.heading('Book Author', text='Book Author')
    tree.heading('Book Genre', text='Book Genre')
    tree.heading('Book Summary', text='Book Summary')
    tree.heading('Status', text='Status')

    # Placing the Treeview widget
    tree.place(x=400, y=50)

    # Back button to return to Admin Dashboard
    back_button = tk.Button(book_management_frame, text="Back", font=("Arial", 14), command=lambda: show_frame(admin_dashboard_frame))
    back_button.place(relx=0.5, rely=0.9, anchor='center')