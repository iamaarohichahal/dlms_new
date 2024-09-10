import tkinter as tk


def show_frame(frame):

    """
    Brings the specified frame to the front, making it visible.
    """
    frame.tkraise()


def display_books(books,browse_books_frame,user_dashboard_frame):
    """
    Displays the list of books in the browse_books_frame.
    Clears any existing widgets before displaying the new list.
    """
    # Clear existing widgets in the frame
    for widget in browse_books_frame.winfo_children():
        widget.destroy()
    
    # Create and place labels for each book
    for index, book in enumerate(books):
        book_label = tk.Label(browse_books_frame, text=f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}, ISBN: {book[4]}", font=("Arial", 12))
        book_label.place(relx=0.5, rely=0.2 + index*0.05, anchor='center')

    # Button to go back to the user dashboard
    back_button = tk.Button(browse_books_frame, text="Back", font=("Arial", 14), command=lambda: show_frame(user_dashboard_frame))
    back_button.place(relx=0.5, rely=0.9, anchor='center')

    show_frame(browse_books_frame)  # Show browse books frame

