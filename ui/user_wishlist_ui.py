import tkinter as tk
import time
from ui.common import show_frame
from tkinter import ttk








def setUp_user_wishlist_frame(user_wishlist_frame, profile_frame):
    # Load the background image
    bg_image = tk.PhotoImage(file=r"C:\Users\iamaa\software\CSIA\dlms\images\bg.png")

    # Add the background image to the frame
    bg_label = tk.Label(user_wishlist_frame, image=bg_image)
    bg_label.image = bg_image  
    bg_label.place(relwidth=1, relheight=1)  # Make it cover the entire frame

    # Title label
    title = tk.Label(user_wishlist_frame, text="My Wishlist", font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
    title.place(x=0, y=0, relwidth=1, height=70)

    # Labels
    book_title_label = tk.Label(user_wishlist_frame, text="Book Title:", font=("Arial", 14), bg="white")
    book_title_label.place(x=100, y=150)

    book_author_label = tk.Label(user_wishlist_frame, text="Book Author:", font=("Arial", 14), bg="white")
    book_author_label.place(x=100, y=200)

    # Read-only Entry Fields
    book_title_entry = tk.Entry(user_wishlist_frame, font=("Arial", 14), state="disabled", width=40)
    book_title_entry.place(x=250, y=150)

    book_author_entry = tk.Entry(user_wishlist_frame, font=("Arial", 14), state="disabled", width=40)
    book_author_entry.place(x=250, y=200)

    # Submit button
    submit_button = tk.Button(user_wishlist_frame, text="Submit", font=("Arial", 14), bg="#4CAF50", fg="white", width=10)
    submit_button.place(relx=0.5, rely=0.7, anchor="center")

    # Back button
    back_button = tk.Button(user_wishlist_frame, text="Back", font=("Arial", 14), command=lambda: show_frame(profile_frame))
    back_button.place(relx=0.5, rely=0.9, anchor="center")
