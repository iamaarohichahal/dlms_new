import tkinter as tk
from tkinter import ttk, messagebox, END
import sqlite3
from db_utils import Database, DB_NAME
from ui.common import show_frame


def populate_book_details(book_list_tree, shared_data):
    selected_book = shared_data.selected_book
    if selected_book:
        # Clear existing items in the Treeview
        book_list_tree.delete(*book_list_tree.get_children())
        # Populate the Treeview with selected book details
        book_list_tree.insert('', 'end', values=(selected_book['title'], selected_book['author'], selected_book['isbn']))

def verify_user_and_borrow(username_entry, password_entry, shared_data):
    username = username_entry.get()
    password = password_entry.get()

    # Connect to the database to verify the user
    conn = sqlite3.connect('dlms.db')
    cursor = conn.cursor()
    
    # Fetch the user record from the database
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()

    # Close the connection
    conn.close()

    if user and user[2] == password:  # Assuming user[2] is the password field
        user_id = user[0]  # Assuming user[0] is the user ID
        messagebox.showinfo('Success', 'User validated')
        # Get the selected book details from shared_data
        selected_book = shared_data.selected_book
        if selected_book:
            book_id = selected_book['id']  # Assuming the 'id' field exists in shared_data for the book
            
            # Borrow the book using the borrow_book method in the Database class
            db = Database()
            db.borrow_book(book_id, user_id)
            
            messagebox.showinfo('Success', 'Book successfully borrowed!')

        else:
            messagebox.showerror('Error', 'No book selected!')

    else:
        messagebox.showerror('Error', 'Invalid username or password')



def setUp_borrow_books_frame(borrow_frame, shared_data, browse_books_frame):

     # Load the background image
    bg_image = tk.PhotoImage(file=r"C:\Users\iamaa\software\CSIA\dlms\images\bg.png")

    # Add the background image to the frame
    bg_label = tk.Label(borrow_frame, image=bg_image)
    bg_label.image = bg_image  
    bg_label.place(relwidth=1, relheight=1)  # Make it cover the entire frame
    # Header
    header_label = tk.Label(borrow_frame, text="Borrow Book", font=("Arial", 16, "bold"), bg="white")
    header_label.place(x=0, y=0, relwidth=1, height=40)  # Place header at top

    # Book Details Treeview
    book_details_label = tk.Label(borrow_frame, text="Book Details", font=("Arial", 14, "bold"), bg="#69359c", fg="white")
    book_details_label.place(x=20, y=50)

    # Creating the Treeview to display the selected book details
    book_list_tree = ttk.Treeview(borrow_frame, height=1, columns=('Title', 'Author', 'ISBN'))
    book_list_tree.column('#0', width=0, stretch=tk.NO)
    book_list_tree.column('Title', anchor=tk.CENTER, width=200)
    book_list_tree.column('Author', anchor=tk.CENTER, width=200)
    book_list_tree.column('ISBN', anchor=tk.CENTER, width=100)

    book_list_tree.heading('Title', text='Title')
    book_list_tree.heading('Author', text='Author')
    book_list_tree.heading('ISBN', text='ISBN')

    book_list_tree.place(x=20, y=100)

    # Populate book details in the tree if available
    selected_book = shared_data.selected_book
    if selected_book:
        book_list_tree.insert('', 'end', values=(selected_book['title'], selected_book['author'], selected_book['isbn']))

    # User Details Section
    user_details_label = tk.Label(borrow_frame, text="User Details", font=("Arial", 14, "bold"), bg="#69359c", fg="white")
    user_details_label.place(x=20, y=350)

    # Username Label and Entry
    username_label = tk.Label(borrow_frame, text="Username:", font=("Arial", 14), bg="white")
    username_label.place(x=20, y=400)
    username_entry = tk.Entry(borrow_frame, font=("Arial", 14), bd=2, width=25, bg="white", fg="black")
    username_entry.place(x=150, y=400)
    username_entry.insert(0, shared_data.get_user_id())  # Automatically fill the username

    # Password Label and Entry
    password_label = tk.Label(borrow_frame, text="Password:", font=("Arial", 14), bg="white")
    password_label.place(x=20, y=450)
    password_entry = tk.Entry(borrow_frame, font=("Arial", 14), bd=2, width=25, bg="white", fg="black", show="*")
    password_entry.place(x=150, y=450)

    # "Populate Details" Button
    populate_details_button = tk.Button(borrow_frame, text="Populate Details", font=("Arial", 14), bg="#1A8F2D", fg="white",
                                         command=lambda: populate_book_details(book_list_tree, shared_data))
    populate_details_button.place(x=20, y=500, width=200, height=30)

    confirm_borrow_button = tk.Button(borrow_frame, text="Confirm Borrow", font=("Arial", 14), bg="#1A8F2D", fg="white",
                                   command=lambda: verify_user_and_borrow(username_entry, password_entry, shared_data))
    confirm_borrow_button.place(x=150, y=550, width=200, height=30)

    # Back button to return to Admin Dashboard
    back_button = tk.Button(borrow_frame, text="Back", font=("Arial", 14), command=lambda: show_frame(browse_books_frame))
    back_button.place(relx=0.5, rely=0.9, anchor='center')