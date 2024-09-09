import tkinter as tk
from tkinter import ttk, messagebox, END
from ui.common import show_frame
from db_utils import Database

import tkinter as tk
from tkinter import messagebox, END
import sqlite3

def clear (id_enter, isbn_enter,book_title_enter, book_author_enter, book_genre_enter, book_summary_enter, book_status_enter):
    id_enter.delete(0,END)
    isbn_enter.delete(0,END)
    book_title_enter.delete(0,END)
    book_author_enter.delete(0,END)
    book_genre_enter.delete(0,END)
    book_summary_enter.delete(0,END)
    book_status_enter.delete(0,END)


def display_book_data(event,tree,id_enter, isbn_enter,book_title_enter, book_author_enter, book_genre_enter, book_summary_enter, book_status_enter):
    print("row is selected")
    selected_item = tree.focus()
    if selected_item:
        row = tree.item(selected_item)['values']
        clear(id_enter, isbn_enter,book_title_enter, book_author_enter, book_genre_enter, book_summary_enter, book_status_enter)
        id_enter.insert(0,row[0])
        isbn_enter.insert(0,row[1])
        book_title_enter.insert(0,row[2])
        book_author_enter.insert(0,row[3])
        book_genre_enter.insert(0,row[4])
        book_summary_enter.insert(0,row[5])
        book_status_enter.insert(0,row[6])
    else:
        pass

def add_books_to_tree(tree):
    database = Database()
    books = database.fetch_books()
    tree.delete(*tree.get_children())
    for book in books:
        tree.insert('', 'end', values=book)

def insert_books_treeview(id_enter, isbn_enter,book_title_enter, book_author_enter, book_genre_enter, book_summary_enter, book_status_enter,tree):
    database = Database()
    id = id_enter.get()
    isbn = isbn_enter.get()
    Book_title = book_title_enter.get()
    Book_author = book_author_enter.get()
    Book_genre = book_genre_enter.get()
    Book_summary = book_summary_enter.get()
    Book_status = book_status_enter.get()
    if not (id and isbn and Book_title and Book_author and Book_genre and Book_summary and Book_status):
        messagebox.showerror('Error', 'Please enter all the fields')
    else:
        database.insert_book(id, isbn, Book_title, Book_author ,Book_genre , Book_summary , Book_status)
        add_books_to_tree(tree)
        messagebox.showinfo('Success', "Your data has been inserted")

def delete_book (id_enter, isbn_enter,book_title_enter, book_author_enter, book_genre_enter, book_summary_enter, book_status_enter,tree):
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Error', 'Chose a book to delete.')
    else:
        id = id_enter.get()
        print("id to be deleted:" + id)
        Database.delete_book(id)
        add_books_to_tree(tree)
        clear(id_enter, isbn_enter,book_title_enter, book_author_enter, book_genre_enter, book_summary_enter, book_status_enter)
        messagebox.showinfo('Success', 'Data has been deleted')

def edit_book(tree, id_enter, isbn_enter,book_title_enter, book_author_enter, book_genre_enter, book_summary_enter, book_status_enter):
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Error', "Choose a book to edit")
    else:
        id = id_enter.get()
        isbn = isbn_enter.get()
        book_title = book_title_enter.get()
        book_author = book_author_enter.get()
        book_genre = book_genre_enter.get()
        book_summary = book_summary_enter.get()
        book_status = book_status_enter.get()
        
        Database.update_book(isbn, book_title, book_author, book_genre, book_summary, book_status, id)

        # Refresh the treeview
        add_books_to_tree(tree)
        
        # Clear the entry fields
        clear(id_enter, isbn_enter,book_title_enter, book_author_enter, book_genre_enter, book_summary_enter, book_status_enter)
        
        messagebox.showinfo('Success', 'Data has been edited')

# -------------------------------------------
# Book Management Frame Setup
# -------------------------------------------
def setUp_book_management(book_management_frame,admin_dashboard_frame):
    # Title label for Book Management Frame
    book_management_label = tk.Label(book_management_frame, text="Book Management", font=("Arial", 20), bg="lightblue")
    book_management_label.pack(pady=10)

    # Labels and Entry fields for Book Details

    id_label = tk.Label(book_management_frame, font=("Arial", 14), text= "ID ", bg="#69359c", fg="white")
    id_label.place(x=20, y=50)

    id_enter = tk.Entry(book_management_frame, font=("Arial", 14), bd=2, width=20, bg="#69359c", fg="white")
    id_enter.place(x=150, y=50)

    isbn_label = tk.Label(book_management_frame, font=("Arial", 14), text= "ISBN ", bg="#69359c", fg="white")
    isbn_label.place(x=20, y=110)

    isbn_enter = tk.Entry(book_management_frame, font=("Arial", 14), bd=2, width=20, bg="#69359c", fg="white")
    isbn_enter.place(x=150, y=110)

    book_title_label = tk.Label(book_management_frame, font=("Arial", 14), text="Book Title", bg="#69359c", fg="white")
    book_title_label.place(x=20, y=170)

    book_title_enter = tk.Entry(book_management_frame, font=("Arial", 14), bd=2, width=20, bg="#69359c", fg="white")
    book_title_enter.place(x=150, y=170)

    book_author_label = tk.Label(book_management_frame, font=("Arial", 14), text="Book Author", bg="#69359c", fg="white")
    book_author_label.place(x=20, y=230)

    book_author_enter = tk.Entry(book_management_frame, font=("Arial", 14), bd=2, width=20, bg="#69359c", fg="white")
    book_author_enter.place(x=150, y=230)

    book_genre_label = tk.Label(book_management_frame, font=("Arial", 14), text="Genre", bg="#69359c", fg="white")
    book_genre_label.place(x=20, y=290)

    book_genre_enter = tk.Entry(book_management_frame, font=("Arial", 14), bd=2, width=20, bg="#69359c", fg="white")
    book_genre_enter.place(x=150, y=290)

    book_summary_label = tk.Label(book_management_frame, font=("Arial", 14), text="Summary", bg="#69359c", fg="white")
    book_summary_label.place(x=20, y=350)

    book_summary_enter = tk.Entry(book_management_frame, font=("Arial", 14), bd=2, width=20, bg="#69359c", fg="white")
    book_summary_enter.place(x=150, y=350)

    book_status_label = tk.Label(book_management_frame, font=("Arial", 14), text="Status", bg="#69359c", fg="white")
    book_status_label.place(x=20, y=410)

    book_status_enter = ttk.Combobox(book_management_frame, font=("Arial", 14), width=18)
    book_status_enter['values'] = ("Available", "Borrowed")  # Set the options in the drop-down
    book_status_enter.place(x=150, y=410)


    # Buttons for User Management Actions
    add_book_button = tk.Button(book_management_frame, font=("Arial", 14), text="Add Book", command=lambda:insert_books_treeview(id_enter, isbn_enter,book_title_enter, book_author_enter, book_genre_enter, book_summary_enter, book_status_enter,tree))
    add_book_button.place(x=20, y=450)

    edit_book_button = tk.Button(book_management_frame, font=("Arial", 14), text="Edit Book", command=lambda:edit_book(tree, id_enter, isbn_enter,book_title_enter, book_author_enter, book_genre_enter, book_summary_enter, book_status_enter))
    edit_book_button.place(x=20, y=500)

    view_book_button = tk.Button(book_management_frame, font=("Arial", 14), text="View Book")
    view_book_button.place(x=20, y=550)

    delete_book_button = tk.Button(book_management_frame, font=("Arial", 14), text="Delete Book", command=lambda:delete_book(id_enter, isbn_enter,book_title_enter, book_author_enter, book_genre_enter, book_summary_enter, book_status_enter,tree))
    delete_book_button.place(x=20, y=600)

    # Styling for the Treeview widget
    style = ttk.Style(book_management_frame)
    style.theme_use('clam')
    style.configure('Treeview', font=("Arial", 14))
    style.map('Treeview', background=[('selected', '#1A8F2D')])

    # Creating the Treeview widget to display book data
    tree = ttk.Treeview(book_management_frame, height=30)

    # Defining columns for the Treeview
    tree['columns'] = ('ID','ISBN', 'Book Title', 'Book Author', 'Book Genre', 'Book Summary', 'Status')


    # Configuring columns
    tree.column('#0', width=0, stretch=tk.NO)
    tree.column('ID', anchor=tk.CENTER, width=50)
    tree.column('ISBN', anchor=tk.CENTER, width=100)
    tree.column('Book Title', anchor=tk.CENTER, width=200)
    tree.column('Book Author', anchor=tk.CENTER, width=200)
    tree.column('Book Genre', anchor=tk.CENTER, width=100)
    tree.column('Book Summary', anchor=tk.CENTER, width=200)
    tree.column('Status', anchor=tk.CENTER, width=100)

    # Defining headings
    tree.heading('ID', text='ID')
    tree.heading('ISBN', text='ISBN')
    tree.heading('Book Title', text='Book Title')
    tree.heading('Book Author', text='Book Author')
    tree.heading('Book Genre', text='Book Genre')
    tree.heading('Book Summary', text='Book Summary')
    tree.heading('Status', text='Status')

    # Placing the Treeview widget
    tree.place(x=400, y=50)

    add_books_to_tree(tree)

    # Back button to return to Admin Dashboard
    back_button = tk.Button(book_management_frame, text="Back", font=("Arial", 14), command=lambda: show_frame(admin_dashboard_frame))
    back_button.place(relx=0.5, rely=0.9, anchor='center')

    # Bind the <<TreeviewSelect>> event to the display_book_data function
    tree.bind('<<TreeviewSelect>>' ,  lambda event: display_book_data(event,tree,id_enter, isbn_enter,book_title_enter, book_author_enter, book_genre_enter, book_summary_enter, book_status_enter))