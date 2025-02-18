import tkinter as tk


def show_frame(frame):
    frame.tkraise()
    


def display_books(books,browse_books_frame,user_dashboard_frame):
    for widget in browse_books_frame.winfo_children():
        widget.destroy()
    
    for index, book in enumerate(books):
        book_label = tk.Label(browse_books_frame, text=f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}, ISBN: {book[4]}", font=("Arial", 12))
        book_label.place(relx=0.5, rely=0.2 + index*0.05, anchor='center')

    back_button = tk.Button(browse_books_frame, text="Back", font=("Arial", 14), command=lambda: show_frame(user_dashboard_frame))
    back_button.place(relx=0.5, rely=0.9, anchor='center')

    show_frame(browse_books_frame)  

