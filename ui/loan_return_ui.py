import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from server.login import Login
from server.loan_management import Loan_management

def populate_return_details(book_list_tree, shared_data):
    """
    Populates the Treeview with details of the selected book for return.
    """
    selected_book = shared_data.selected_book
    if selected_book:
        # Clear existing items in the Treeview
        book_list_tree.delete(*book_list_tree.get_children())
        # Insert the selected book details into the Treeview
        book_list_tree.insert('', 'end', values=(selected_book['title'], selected_book['author']))
    else:
        messagebox.showinfo("No Selection", "No book has been selected for return.")


def verify_user_and_return(username_entry, password_entry, shared_data):
    """
    Validates the user and removes the selected book's record from the borrowed_books table.
    """
    username = username_entry.get()
    password = password_entry.get()

    try:

        login = Login()
        
        if login.validate_user('non_admin', username, password) == True:
    
            user_id = username
            messagebox.showinfo('Success', 'User validated')

            # Get the selected book details from shared_data
            selected_book = shared_data.selected_book
            if selected_book:
                book_id = selected_book['book_id']  # Assuming 'id' is the book ID in shared_data

                # Check if the book exists in the borrowed_books table for this user
                loan_management = Loan_management()

                status = loan_management.return_borrowed_book(book_id,user_id)

                if  status == True: 
                    messagebox.showinfo('Success', 'Book successfully returned!')
                else:
                    messagebox.showerror('Error', 'This book is not recorded as borrowed by the user.')
            else:
                messagebox.showerror('Error', 'No book selected for return!')
        else:
            messagebox.showerror('Error', 'Invalid username or password')
    except sqlite3.Error as e:
        messagebox.showerror('Database Error', f"An error occurred: {e}")

import tkinter as tk
from tkinter import ttk

def setUp_loan_return_frame(loan_return_frame, show_frame, loan_details_frame, shared_data):
    # Load the background image
    bg_image = tk.PhotoImage(file=r"C:\Users\iamaa\software\CSIA\dlms\images\bg.png")

    # Add the background image to the frame
    bg_label = tk.Label(loan_return_frame, image=bg_image)
    bg_label.image = bg_image  
    bg_label.place(relwidth=1, relheight=1)  # Make it cover the entire frame
    
    # Title label for Loan Return Frame
    loan_return_label = tk.Label(
        loan_return_frame,
        text="Loan Return",
        font=("times new roman", 40, "bold"),
        bg="#69359c",
        fg="white"
    )
    loan_return_label.place(x=0, y=0, relwidth=1, height=70)

    # Create a wider frame for book details section (lowered slightly)
    book_details_frame = tk.Frame(loan_return_frame, bd=2, relief="ridge", bg="white")
    book_details_frame.place(relx=0.5, rely=0.25, anchor="center", width=800, height=250)  # Centered it properly

    # Treeview section for Book Details (Centered inside book_details_frame)
    book_list_tree = ttk.Treeview(book_details_frame, height=3, columns=('Title', 'Author'))
    book_list_tree.column('#0', width=0, stretch=tk.NO)  # Hide default column
    book_list_tree.column('Title', anchor=tk.W, width=380)  # Increased width slightly
    book_list_tree.column('Author', anchor=tk.W, width=380)

    book_list_tree.heading('Title', text='Title', anchor=tk.W)
    book_list_tree.heading('Author', text='Author', anchor=tk.W)

    book_list_tree.pack(pady=20, padx=15, fill="both")  # Adjusted padding to center it properly

    # Populate details button (Centered inside book_details_frame)
    populate_details_button = tk.Button(
        book_details_frame,
        text="Populate Book Details",
        font=("Arial", 14),
        bg="#1A8F2D",
        fg="white",
        width=20, height=2,
        command=lambda: populate_return_details(book_list_tree, shared_data)
    )
    populate_details_button.pack(pady=10)  # Ensured proper centering below Treeview

    # Create a frame for User Details (Aligned with Book Details Frame)
    user_details_frame = tk.Frame(loan_return_frame, bd=2, relief="ridge", bg="white")
    user_details_frame.place(relx=0.5, rely=0.6, anchor="center", width=800, height=250)


    # Username Field
    username_label = tk.Label(loan_return_frame, text="Username:", font=("Arial", 14), bg="white")
    username_label.place(relx=0.3, rely=0.52, anchor='center')

    username_entry = tk.Entry(loan_return_frame, font=("Arial", 14), bd=2, width=30, bg="white", fg="black")
    username_entry.place(relx=0.55, rely=0.52, anchor='center')
    username_entry.insert(0, shared_data.get_user_id())  # Autofill username

    # Password Field
    password_label = tk.Label(loan_return_frame, text="Password:", font=("Arial", 14), bg="white")
    password_label.place(relx=0.3, rely=0.58, anchor='center')

    password_entry = tk.Entry(loan_return_frame, font=("Arial", 14), bd=2, width=30, bg="white", fg="black", show="*")
    password_entry.place(relx=0.55, rely=0.58, anchor='center')

    # Confirm Return Button
    confirm_return_button = tk.Button(
        loan_return_frame,
        text="Confirm Return",
        font=("Arial", 14),
        bg="#1A8F2D",
        fg="white",
        width=20, height=2,
        command=lambda: verify_user_and_return(username_entry, password_entry, shared_data)
    )
    confirm_return_button.place(relx=0.5, rely=0.68, anchor='center')

    # Back Button
    back_button = tk.Button(
        loan_return_frame,
        text="Back",
        font=("Arial", 14),
        bg="#1A8F2D",
        fg="white",
        width=20, height=2,
        command=lambda: show_frame(loan_details_frame)
    )
    back_button.place(relx=0.5, rely=0.9, anchor='center') 
