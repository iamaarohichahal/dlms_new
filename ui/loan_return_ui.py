import tkinter as tk
from tkinter import ttk, messagebox, END
from db_utils import Database
import sqlite3

def populate_return_details(book_list_tree, shared_data):
    """
    Populates the Treeview with details of the selected book for return.
    """
    selected_book = shared_data.selected_book
    if selected_book:
        # Clear existing items in the Treeview
        book_list_tree.delete(*book_list_tree.get_children())
        # Insert the selected book details into the Treeview
        book_list_tree.insert('', 'end', values=(selected_book['title'], selected_book['author'], selected_book['isbn']))
    else:
        messagebox.showinfo("No Selection", "No book has been selected for return.")


def verify_user_and_return(username_entry, password_entry, shared_data):
    """
    Validates the user and removes the selected book's record from the borrowed_books table.
    """
    username = username_entry.get()
    password = password_entry.get()

    # Connect to the database to verify the user
    conn = sqlite3.connect('dlms.db')
    cursor = conn.cursor()

    try:
        # Fetch the user record from the database
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()

        if user and user[2] == password:  # Assuming user[2] is the password field
            user_id = user[0]  # Assuming user[0] is the user ID
            messagebox.showinfo('Success', 'User validated')

            # Get the selected book details from shared_data
            selected_book = shared_data.selected_book
            if selected_book:
                book_id = selected_book['book_id']  # Assuming 'id' is the book ID in shared_data

                # Check if the book exists in the borrowed_books table for this user
                cursor.execute(
                    'SELECT * FROM borrowed_books WHERE book_id = ? AND user_id = ?',
                    (book_id, user_id)
                )
                borrowed_book = cursor.fetchone()

                if borrowed_book:
                    # Remove the book from the borrowed_books table
                    cursor.execute(
                        'DELETE FROM borrowed_books WHERE book_id = ? AND user_id = ?',
                        (book_id, user_id)
                    )
                    conn.commit()
                    messagebox.showinfo('Success', 'Book successfully returned!')
                else:
                    messagebox.showerror('Error', 'This book is not recorded as borrowed by the user.')
            else:
                messagebox.showerror('Error', 'No book selected for return!')
        else:
            messagebox.showerror('Error', 'Invalid username or password')
    except sqlite3.Error as e:
        messagebox.showerror('Database Error', f"An error occurred: {e}")
    finally:
        conn.close()


def setUp_loan_return_frame(loan_return_frame, show_frame, loan_details_frame, shared_data):

     # Load the background image
    bg_image = tk.PhotoImage(file=r"C:\Users\iamaa\software\CSIA\dlms\images\bg.png")

    # Add the background image to the frame
    bg_label = tk.Label(loan_return_frame, image=bg_image)
    bg_label.image = bg_image  
    bg_label.place(relwidth=1, relheight=1)  # Make it cover the entire frame
    """
    Sets up the Loan Return frame, including Treeview for book details and user confirmation inputs.
    """
    # Frame title
    loan_return_label = tk.Label(
        loan_return_frame,
        text="Return Book",
        font=("Arial", 20),
        bg="lightblue"
    )
    loan_return_label.pack(pady=10)

    # Treeview section for Book Details
    book_details_label = tk.Label(
        loan_return_frame,
        text="Selected Book Details",
        font=("Arial", 14, "bold"),
        bg="#69359c",
        fg="white"
    )
    book_details_label.place(x=20, y=50)

    # Treeview setup for displaying book details
    book_list_tree = ttk.Treeview(loan_return_frame, height=1, columns=('Title', 'Author', 'ISBN'))
    book_list_tree.column('#0', width=0, stretch=tk.NO)  # Hide default column
    book_list_tree.column('Title', anchor=tk.CENTER, width=200)
    book_list_tree.column('Author', anchor=tk.CENTER, width=200)
    book_list_tree.column('ISBN', anchor=tk.CENTER, width=150)

    book_list_tree.heading('Title', text='Title')
    book_list_tree.heading('Author', text='Author')
    book_list_tree.heading('ISBN', text='ISBN')

    book_list_tree.place(x=20, y=100)

    # Populate details button
    populate_details_button = tk.Button(
        loan_return_frame,
        text="Populate Book Details",
        font=("Arial", 14),
        bg="#1A8F2D",
        fg="white",
        command=lambda: populate_return_details(book_list_tree, shared_data)
    )
    populate_details_button.place(x=20, y=150, width=200, height=30)

    # User confirmation details
    user_details_label = tk.Label(
        loan_return_frame,
        text="User Details",
        font=("Arial", 14, "bold"),
        bg="#69359c",
        fg="white"
    )
    user_details_label.place(x=20, y=200)

    # Username field
    username_label = tk.Label(
        loan_return_frame,
        text="Username:",
        font=("Arial", 14),
        bg="white"
    )
    username_label.place(x=20, y=250)
    username_entry = tk.Entry(
        loan_return_frame,
        font=("Arial", 14),
        bd=2,
        width=25,
        bg="white",
        fg="black"
    )
    username_entry.place(x=150, y=250)
    username_entry.insert(0, shared_data.get_user_id())  # Autofill username

    # Password field
    password_label = tk.Label(
        loan_return_frame,
        text="Password:",
        font=("Arial", 14),
        bg="white"
    )
    password_label.place(x=20, y=300)
    password_entry = tk.Entry(
        loan_return_frame,
        font=("Arial", 14),
        bd=2,
        width=25,
        bg="white",
        fg="black",
        show="*"
    )
    password_entry.place(x=150, y=300)

    confirm_return_button = tk.Button(
    loan_return_frame,
    text="Confirm Return",
    font=("Arial", 14),
    bg="#1A8F2D",
    fg="white",
    command=lambda: verify_user_and_return(username_entry, password_entry, shared_data)
)
    confirm_return_button.place(x=20, y=350, width=200, height=30)



    #Button
    back_button = tk.Button(loan_return_frame, text="Back", font=("Arial", 14), command=lambda: show_frame(loan_details_frame))
    back_button.place(relx=0.6, rely=0.9, anchor='center')