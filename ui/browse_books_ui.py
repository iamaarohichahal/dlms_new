import tkinter as tk
import sqlite3
from tkinter import ttk, END
from db_utils import Database,DB_NAME



def add_book_list_to_tree(book_list_tree):
    database = Database()
    books = database.fetch_book_list()
    book_list_tree.delete(*book_list_tree.get_children())
    for book in books:
        book_list_tree.insert('', 'end', values=book)

def clear (title_enter, author_enter, isbn_enter, summary_text):
    title_enter.delete(0,END)
    author_enter.delete(0,END)
    isbn_enter.delete(0,END)
    # Clear the Text widget (summary_text)
    summary_text.delete(1.0, tk.END)

def display_book_details(event, book_list_tree, title_enter, author_enter, isbn_enter, summary_text,shared_data):
    print("logged user:" + shared_data.get_user_id())
       # Get the selected item from the Treeview
    selected_item = book_list_tree.focus()
    
    if selected_item:
        row = book_list_tree.item(selected_item)['values']
        book_id = row[0]  
        clear(title_enter, author_enter, isbn_enter, summary_text)
        conn = sqlite3.connect(DB_NAME) 
        cursor = conn.cursor()
        
        cursor.execute("SELECT title, author, isbn, summary FROM books WHERE id=?", (book_id,))
        book_details = cursor.fetchone()

        if book_details:

            title_enter.insert(0, book_details[0]) 
            author_enter.insert(0, book_details[1])  
            isbn_enter.insert(0, book_details[2])  
            summary_text.insert(1.0, book_details[3]) 
        
    
        conn.close()
    else:
        pass  

   

def setUp_browse_books(browse_books_frame,shared_data):

    # Create the frame
    book_details = tk.Frame(browse_books_frame, bd=2, relief="ridge", bg="white", height=700)
    book_details.place(x=1000, y=100, width=400, height=700)

    # Header
    header_label = tk.Label(book_details, text="Book Details", font=("Arial", 16, "bold"), bg="white")
    header_label.place(x=0, y=0, relwidth=1, height=20)  # Place header at top


    # Labels and Entry boxes
   
    # Title
    title_label = tk.Label(book_details, font=("Arial", 14), text="Title", bg="#69359c", fg="white")
    title_label.place(x=20, y=60)

    title_enter = tk.Entry(book_details, font=("Arial", 14), bd=2, width=25, bg="white", fg="black")
    title_enter.place(x=100, y=60)

    # Author
    author_label = tk.Label(book_details, font=("Arial", 14), text="Author", bg="#69359c", fg="white")
    author_label.place(x=20, y=120)

    author_enter = tk.Entry(book_details, font=("Arial", 14), bd=2, width=25, bg="white", fg="black")
    author_enter.place(x=100, y=120)

    # ISBN
    isbn_label = tk.Label(book_details, font=("Arial", 14), text="ISBN", bg="#69359c", fg="white")
    isbn_label.place(x=20, y=180)

    isbn_enter = tk.Entry(book_details, font=("Arial", 14), bd=2, width=25, bg="white", fg="black")
    isbn_enter.place(x=100, y=180)

    # Summary
    summary_label = tk.Label(book_details, font=("Arial", 14), text="summary", bg="#69359c", fg="white")
    summary_label.place(x=20, y=240)

    summary_text = tk.Text(book_details, font=("Arial", 14), bd=2, bg="white", fg="black", wrap=tk.WORD)
    summary_text.place(x=110, y=240, width=250, height=350) 

     # username
    username_label = tk.Label(book_details, font=("Arial", 14), text="username", bg="#69359c", fg="white")
    username_label.place(x=20, y=610)

    username_enter = tk.Entry(book_details, font=("Arial", 14), bd=2, width=15, bg="white", fg="black")
    username_enter.place(x=115, y=610)
 
   # username_enter.insert(0, shared_data.get_user_id())


    # "Borrow" Button
    borrow_button = tk.Button(book_details, text="Borrow", font=("Arial", 14), bg="#1A8F2D", fg="white", bd=2)
    borrow_button.place(x=150, y=650, width=100, height=30)

    # Styling for the Treeview widget for list of books
    style = ttk.Style(browse_books_frame)
    style.theme_use('clam')
    style.configure('Treeview', font=("Arial", 14))
    style.map('Treeview', background=[('selected', '#1A8F2D')])

    # Creating the Treeview widget to display book list
    book_list_tree = ttk.Treeview(browse_books_frame, height=30, columns=('ID','Book Title', 'Book Author', 'Status'))

    # Configuring columns
    book_list_tree.column('#0', width=0, stretch=tk.NO)
    book_list_tree.column('ID', anchor=tk.CENTER, width=50)
    book_list_tree.column('Book Title', anchor=tk.CENTER, width=400)
    book_list_tree.column('Book Author', anchor=tk.CENTER, width=400)
    book_list_tree.column('Status', anchor=tk.CENTER, width=100)

    # Defining headings
    book_list_tree.heading('ID', text='ID')
    book_list_tree.heading('Book Title', text='Book Title')
    book_list_tree.heading('Book Author', text='Book Author')
    book_list_tree.heading('Status', text='Status')

    add_book_list_to_tree(book_list_tree)

    book_list_tree.bind('<<TreeviewSelect>>' ,  lambda event: display_book_details(event,book_list_tree,title_enter,author_enter ,isbn_enter,summary_text,shared_data))
    # Placing the Treeview widget
    book_list_tree.place(x=20, y=100)


