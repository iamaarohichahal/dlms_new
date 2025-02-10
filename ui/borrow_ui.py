import tkinter as tk
from tkinter import ttk, messagebox
from ui.common import show_frame
from server.login import Login
from server.loan_management import Loan_management


def populate_book_details(book_list_tree, shared_data):
    selected_book = shared_data.selected_book
    if selected_book:
     
        book_list_tree.delete(*book_list_tree.get_children())
        # Populate the Treeview with selected book details
        book_list_tree.insert('', 'end', values=(selected_book['title'], selected_book['author'], selected_book['isbn']))

def verify_user_and_borrow(username_entry, password_entry, shared_data):
    username = username_entry.get()
    password = password_entry.get()
    login = Login()

    if login.validate_user('non_admin', username, password) == True:  
        user_id = username 
        messagebox.showinfo('Success', 'User validated')
        
       
        selected_book = shared_data.selected_book
        if selected_book:
            book_id = selected_book['id']  
            
            loan_management = Loan_management()

            if loan_management.borrow_book(user_id, book_id) == True:

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
    header_label = tk.Label(borrow_frame, text="Borrow Book", font=("Arial", 20, "bold"), bg="#69359c", fg="white")
    header_label.place(x=0, y=0, relwidth=1, height=50)  # Updated header style

    # Create a wider frame for book details section (lowered slightly)
    book_details_frame = tk.Frame(borrow_frame, bd=2, relief="ridge", bg="white")
    book_details_frame.place(x=150, y=70, width=1100, height=250)  # Centered it properly
    

    # Creating the Treeview to display the selected book details
    book_list_tree = ttk.Treeview(borrow_frame, height=1, columns=('Title', 'Author', 'ISBN'))
    book_list_tree.column('#0', width=0, stretch=tk.NO)
    book_list_tree.column('Title', anchor=tk.CENTER, width=400)
    book_list_tree.column('Author', anchor=tk.CENTER, width=200)
    book_list_tree.column('ISBN', anchor=tk.CENTER, width=400)

    book_list_tree.heading('Title', text='Title')
    book_list_tree.heading('Author', text='Author')
    book_list_tree.heading('ISBN', text='ISBN')

    book_list_tree.place(x=200, y=100)

    # Populate book details in the tree if available
    selected_book = shared_data.selected_book
    if selected_book:
        book_list_tree.insert('', 'end', values=(selected_book['title'], selected_book['author'], selected_book['isbn']))

    # Create a wider frame for book details section (lowered slightly)
    user_details_frame = tk.Frame(borrow_frame, bd=2, relief="ridge", bg="white")
    user_details_frame.place(x=150, y=370, width=1100, height=250)  # Centered it properly

    # Username Label and Entry
    username_label = tk.Label(borrow_frame, text="Username:", font=("Arial", 14), bg="white")
    username_label.place(x=450, y=400)
    username_entry = tk.Entry(borrow_frame, font=("Arial", 14), bd=2, width=25, bg="white", fg="black")
    username_entry.place(x=700, y=400)
    username_entry.insert(0, shared_data.get_user_id())  # Automatically fill the username

    # Password Label and Entry
    password_label = tk.Label(borrow_frame, text="Password:", font=("Arial", 14), bg="white")
    password_label.place(x=450, y=450)
    password_entry = tk.Entry(borrow_frame, font=("Arial", 14), bd=2, width=25, bg="white", fg="black", show="*")
    password_entry.place(x=700, y=450)


        # "Populate Details" Button
    populate_details_button = tk.Button(
        borrow_frame,
        text="Populate Details",
        font=("Arial", 14),
        bg="#1A8F2D",
        fg="white",
        width=20, height=2,
        command=lambda: populate_book_details(book_list_tree, shared_data)
    )
    populate_details_button.place(x=650, y=250, width=200, height=40)

    # "Confirm Borrow" Button
    confirm_borrow_button = tk.Button(
        borrow_frame,
        text="Confirm Borrow",
        font=("Arial", 14),
        bg="#1A8F2D",
        fg="white",
        width=20, height=2,
        command=lambda: verify_user_and_borrow(username_entry, password_entry, shared_data)
    )
    confirm_borrow_button.place(x=650, y=550, width=200, height=40)

    # Back button
    back_button = tk.Button(
        borrow_frame,
        text="Back",
        font=("Arial", 14),
        bg="#1A8F2D",
        fg="white",
        width=20, height=2,
        command=lambda: show_frame(browse_books_frame)
    )
    back_button.place(relx=0.5, rely=0.9, anchor='center', width=150, height=40)