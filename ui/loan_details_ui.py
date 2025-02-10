import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from ui.common import show_frame
from server.loan_management import Loan_management

def view_loans(shared_data, loan_details_tree):
    """
    Fetches and populates the Treeview with book details (ID, ISBN, Title, Author, Genre, Summary, Return Date)
    for the borrowed books corresponding to the logged-in user.
    """
    # Retrieve the user_id from shared data (this will be the ID of the logged-in user)
    user_id = shared_data.get_user_id()  # Assuming shared_data has a get_user_id() method

    if user_id:  # Ensure user_id is valid (logged in)

        try:
            # Fetch borrowed books and corresponding book details for the logged-in user

            loan_management = Loan_management()

            borrowed_books = loan_management.get_loans(user_id)

            if borrowed_books:
                # Clear the Treeview before adding new rows
                loan_details_tree.delete(*loan_details_tree.get_children())
                
                # Loop through the fetched data and insert into Treeview
                for book in borrowed_books:
                    book_id, title, author, genre, return_date = book
                    loan_details_tree.insert('', 'end', values=(book_id, title, author, genre, return_date))
            else:
                print("No borrowed books found.")
        
        except sqlite3.Error as e:
            print(f"Error fetching borrowed books: {e}")
    else:
        print("User is not logged in.")

def handle_return_book(loan_details_tree, loan_return_frame, loan_details_frame, shared_data):
    """
    Handles the 'Return Book' button action. Opens a new frame for returning a book
    if a row is selected in the Treeview.
    """
    # Get the selected item from the Treeview
    selected_item = loan_details_tree.selection()
    
    if selected_item:
        # Fetch data from the selected row
        selected_book = loan_details_tree.item(selected_item[0], 'values')
        shared_data.selected_book = {
            'book_id': selected_book[0],
            'title': selected_book[1],
            'author': selected_book[2],
            'genre': selected_book[3],
            'return_date': selected_book[4],
        }
        
        # Show the Loan Return Frame
        show_frame(loan_return_frame)
    else:
        # Display error message if no row is selected
        messagebox.showerror("Error", "Please select a book to return.")





# -------------------------------------------
# Loan Details Frame Setup
# -------------------------------------------
def setUp_loan_details(loan_details_frame, user_dashboard_frame, shared_data, loan_return_frame):
    # Load the background image
    bg_image = tk.PhotoImage(file=r"C:\Users\iamaa\software\CSIA\dlms\images\bg.png")

    # Add the background image to the frame
    bg_label = tk.Label(loan_details_frame, image=bg_image)
    bg_label.image = bg_image  
    bg_label.place(relwidth=1, relheight=1)  # Make it cover the entire frame

    # Title label for Loan Details Frame
    loan_details_label = tk.Label(loan_details_frame, text="Loan Details", font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
    loan_details_label.place(x=0, y=0, relwidth=1, height=70)

    # Styling for the Treeview widget
    style = ttk.Style(loan_details_frame)
    style.theme_use('clam')
    style.configure('Treeview', font=("Arial", 14))
    style.map('Treeview', background=[('selected', '#1A8F2D')])

    # Creating the Treeview widget to display book data
    loan_details_tree = ttk.Treeview(loan_details_frame, height=18)  

    # Defining columns for the Treeview
    loan_details_tree['columns'] = ('ID', 'Book Title', 'Book Author', 'Book Genre', 'Return Date')

    # Configuring columns
    loan_details_tree.column('#0', width=0, stretch=tk.NO)
    loan_details_tree.column('ID', anchor=tk.CENTER, width=50)
    loan_details_tree.column('Book Title', anchor=tk.CENTER, width=250)
    loan_details_tree.column('Book Author', anchor=tk.CENTER, width=250)
    loan_details_tree.column('Book Genre', anchor=tk.CENTER, width=150)
    loan_details_tree.column('Return Date', anchor=tk.CENTER, width=200)

    # Defining headings
    loan_details_tree.heading('ID', text='ID')
    loan_details_tree.heading('Book Title', text='Book Title')
    loan_details_tree.heading('Book Author', text='Book Author')
    loan_details_tree.heading('Book Genre', text='Book Genre')
    loan_details_tree.heading('Return Date', text='Return Date')

    # Place the Treeview widget to take up most of the screen
    loan_details_tree.place(relx=0.5, rely=0.45, anchor='center', relwidth=0.9, relheight=0.7)  

    # Buttons for Return Book, Back, and View Loans
    button_width = 20
    button_height = 2

    return_button = tk.Button(loan_details_frame, text="Return Book", font=("Arial", 16, "bold"), bg="#4CAF50", fg="white",
                              width=button_width, height=button_height, relief="solid",
                              command=lambda: handle_return_book(loan_details_tree, loan_return_frame, loan_details_frame, shared_data))
    return_button.place(relx=0.25, rely=0.9, anchor='center')

    back_button = tk.Button(loan_details_frame, text="Back", font=("Arial", 16, "bold"), bg="#4CAF50", fg="white",
                            width=button_width, height=button_height, relief="solid",
                            command=lambda: show_frame(user_dashboard_frame))
    back_button.place(relx=0.5, rely=0.9, anchor='center')

    view_loans_button = tk.Button(loan_details_frame, text="View Loans", font=("Arial", 16, "bold"), bg="#4CAF50", fg="white",
                                  width=button_width, height=button_height, relief="solid",
                                  command=lambda: view_loans(shared_data, loan_details_tree))
    view_loans_button.place(relx=0.75, rely=0.9, anchor='center')
