import tkinter as tk
from ui.common import show_frame
from server.book_management import Book
from tkinter import messagebox




def submit_wishlist(book_title_entry,book_author_entry,shared_data):
    book_title = book_title_entry.get()
    book_author = book_author_entry.get()
    book = Book()
    book.author = book_author
    book.title = book_title
    wishlist_queue = shared_data.get_wishlist_queue()
    wishlist_queue.put(book)
    messagebox.showinfo('Success!' , 'Book added to wishlist')


    



def setUp_user_wishlist_frame(user_wishlist_frame, profile_frame,shared_data):

    bg_image = tk.PhotoImage(file=r"C:\Users\iamaa\software\CSIA\dlms\images\bg.png")

    bg_label = tk.Label(user_wishlist_frame, image=bg_image)
    bg_label.image = bg_image  
    bg_label.place(relwidth=1, relheight=1)  

    title = tk.Label(user_wishlist_frame, text="My Wishlist", font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
    title.place(x=0, y=0, relwidth=1, height=70)

    book_title_label = tk.Label(user_wishlist_frame, text="Book Title:", font=("Arial", 14), bg="white")
    book_title_label.place(x=100, y=150)

    book_author_label = tk.Label(user_wishlist_frame, text="Book Author:", font=("Arial", 14), bg="white")
    book_author_label.place(x=100, y=200)

    book_title_entry = tk.Entry(user_wishlist_frame, font=("Arial", 14), width=40)
    book_title_entry.place(x=250, y=150)

    book_author_entry = tk.Entry(user_wishlist_frame, font=("Arial", 14), width=40)
    book_author_entry.place(x=250, y=200)

    submit_button = tk.Button(user_wishlist_frame, text="Submit", font=("Arial", 14), bg="#4CAF50", fg="white", width=10, command=lambda:submit_wishlist(book_title_entry,book_author_entry,shared_data))
    submit_button.place(relx=0.5, rely=0.7, anchor="center")

    back_button = tk.Button(user_wishlist_frame, text="Back", font=("Arial", 14), command=lambda: show_frame(profile_frame))
    back_button.place(relx=0.5, rely=0.9, anchor="center")
