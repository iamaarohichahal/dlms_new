import tkinter as tk
from tkinter import ttk, END
from ui.common import show_frame
from server.book_management import Book




def add_book_list_to_tree(book_list_tree):

    book_management = Book()
    
    sorted_books = book_management.get_books()

    book_list_tree.delete(*book_list_tree.get_children())

    for book in sorted_books:

        book_list_tree.insert('', 'end', values=book)

def clear (title_enter, author_enter, isbn_enter, summary_text,id_enter):
    title_enter.delete(0,END)
    author_enter.delete(0,END)
    isbn_enter.delete(0,END)
    id_enter.delete(0,END)

    summary_text.delete(1.0, tk.END)

def display_book_details(event, book_list_tree, title_enter, author_enter, isbn_enter, summary_text,shared_data,id_enter):
    print("logged user:" + shared_data.get_user_id())

    selected_item = book_list_tree.focus()
    
    if selected_item:
        row = book_list_tree.item(selected_item)['values']
        book_id = row[0]  
        clear(title_enter, author_enter, isbn_enter, summary_text,id_enter)
        
        book_management = Book()

        book_details = book_management.get_book(book_id)
        if book_details:
            print(book_details)
            id_enter.insert(0,book_id)
            title_enter.insert(0, book_details[0]) 
            author_enter.insert(0, book_details[1])  
            isbn_enter.insert(0, book_details[2])  
            summary_text.insert(1.0, book_details[3]) 
    else:
        pass  

def borrow_book(id, title, author, isbn, summary, borrow_frame, shared_data):
    shared_data.selected_book = {
        'id' : id,
        'title': title,
        'author': author,
        'isbn': isbn,
        'summary': summary
    }
    show_frame(borrow_frame)

def search_books_by_coloumn(coloumn,search_title_entry, book_list_tree):
   
    search_term = search_title_entry.get().strip().lower()
    if not search_term:

        add_book_list_to_tree(book_list_tree)
        return
    
    book_management = Book()

    filtered_books = book_management.search_books(coloumn,search_term)


    book_list_tree.delete(*book_list_tree.get_children()) 
    for book in filtered_books:
        book_list_tree.insert('', 'end', values=book)


   
def setUp_browse_books(browse_books_frame, shared_data, borrow_frame,user_dashboard_frame):


    bg_image = tk.PhotoImage(file=r"C:\Users\iamaa\software\CSIA\dlms\images\bg.png")

  
    bg_label = tk.Label(browse_books_frame, image=bg_image)
    bg_label.image = bg_image  
    bg_label.place(relwidth=1, relheight=1) 

    book_details = tk.Frame(browse_books_frame, bd=2, relief="ridge", bg="white", height=700)
    book_details.place(x=1000, y=100, width=400, height=700)


    header_label = tk.Label(book_details, text="Book Details", font=("Arial", 16, "bold"), bg="white")
    header_label.place(x=0, y=0, relwidth=1, height=20)  



    search_frame = tk.Frame(browse_books_frame, bd=2, relief="ridge", bg="white")
    search_frame.place(x=20, y=100, width=900, height=200)

 
    search_isbn_label = tk.Label(search_frame, font=("Arial", 14), text="ISBN", bg="#69359c", fg="white")
    search_isbn_label.grid(row=0, column=0, padx=10, pady=10)

    search_isbn_entry = tk.Entry(search_frame, font=("Arial", 14), bd=2, width=20, bg="white", fg="black")
    search_isbn_entry.grid(row=0, column=1, padx=10, pady=10)

    search_title_label = tk.Label(search_frame, font=("Arial", 14), text="Title", bg="#69359c", fg="white")
    search_title_label.grid(row=0, column=2, padx=10, pady=10)

    search_title_entry = tk.Entry(search_frame, font=("Arial", 14), bd=2, width=20, bg="white", fg="black")
    search_title_entry.grid(row=0, column=3, padx=10, pady=10)


    search_author_label = tk.Label(search_frame, font=("Arial", 14), text="Author", bg="#69359c", fg="white")
    search_author_label.grid(row=1, column=0, padx=10, pady=10)

    search_author_entry = tk.Entry(search_frame, font=("Arial", 14), bd=2, width=20, bg="white", fg="black")
    search_author_entry.grid(row=1, column=1, padx=10, pady=10)


    search_genre_label = tk.Label(search_frame, font=("Arial", 14), text="Genre", bg="#69359c", fg="white")
    search_genre_label.grid(row=1, column=2, padx=10, pady=10)

    search_genre_entry = tk.Entry(search_frame, font=("Arial", 14), bd=2, width=20, bg="white", fg="black")
    search_genre_entry.grid(row=1, column=3, padx=10, pady=10)

    search_isbn_button = tk.Button(search_frame, text="Search by ISBN", font=("Arial", 14), bg="#1A8F2D", fg="white", bd=2, command=lambda: search_books_by_coloumn('isbn',search_isbn_entry, book_list_tree))
    search_isbn_button.grid(row=2, column=0, pady=10)

    search_title_button = tk.Button(search_frame, text="Search by Title", font=("Arial", 14), bg="#1A8F2D", fg="white", bd=2, command=lambda: search_books_by_coloumn('title', search_title_entry, book_list_tree))
    search_title_button.grid(row=2, column=1, pady=10)

    search_author_button = tk.Button(search_frame, text="Search by Author", font=("Arial", 14), bg="#1A8F2D", fg="white", bd=2, command=lambda: search_books_by_coloumn('author', search_author_entry, book_list_tree))
    search_author_button.grid(row=2, column=2, pady=10)

    search_genre_button = tk.Button(search_frame, text="Search by Genre", font=("Arial", 14), bg="#1A8F2D", fg="white", bd=2, command=lambda: search_books_by_coloumn('genre', search_genre_entry, book_list_tree))
    search_genre_button.grid(row=2, column=3, pady=10)


    id_label = tk.Label(book_details, font=("Arial", 14), text="ID", bg="#69359c", fg="white")
    id_label.place(x=20, y=60)

    id_enter = tk.Entry(book_details, font=("Arial", 14), bd=2, width=25, bg="white", fg="black")
    id_enter.place(x=100, y=60)


    title_label = tk.Label(book_details, font=("Arial", 14), text="Title", bg="#69359c", fg="white")
    title_label.place(x=20, y=100)

    title_enter = tk.Entry(book_details, font=("Arial", 14), bd=2, width=25, bg="white", fg="black")
    title_enter.place(x=100, y=100)

    author_label = tk.Label(book_details, font=("Arial", 14), text="Author", bg="#69359c", fg="white")
    author_label.place(x=20, y=140)

    author_enter = tk.Entry(book_details, font=("Arial", 14), bd=2, width=25, bg="white", fg="black")
    author_enter.place(x=100, y=140)


    isbn_label = tk.Label(book_details, font=("Arial", 14), text="ISBN", bg="#69359c", fg="white")
    isbn_label.place(x=20, y=180)

    isbn_enter = tk.Entry(book_details, font=("Arial", 14), bd=2, width=25, bg="white", fg="black")
    isbn_enter.place(x=100, y=180)


    summary_label = tk.Label(book_details, font=("Arial", 14), text="Summary", bg="#69359c", fg="white")
    summary_label.place(x=20, y=240)

    summary_text = tk.Text(book_details, font=("Arial", 14), bd=2, bg="white", fg="black", wrap=tk.WORD)
    summary_text.place(x=110, y=240, width=250, height=350)

   

    borrow_button = tk.Button(book_details, text="Borrow", font=("Arial", 14), bg="#1A8F2D", fg="white", bd=2,command=lambda: borrow_book(id_enter.get(), title_enter.get(), author_enter.get(), isbn_enter.get(), summary_text.get("1.0", "end-1c"), borrow_frame, shared_data))
    borrow_button.place(x=150, y=650, width=100, height=30)

    style = ttk.Style(browse_books_frame)
    style.theme_use('clam')
    style.configure('Treeview', font=("Arial", 14))
    style.map('Treeview', background=[('selected', '#1A8F2D')])

    book_list_tree = ttk.Treeview(browse_books_frame, height=20, columns=('ID', 'Book Title', 'Book Author', 'Status'))

    book_list_tree.column('#0', width=0, stretch=tk.NO)
    book_list_tree.column('ID', anchor=tk.CENTER, width=50)
    book_list_tree.column('Book Title', anchor=tk.CENTER, width=400)
    book_list_tree.column('Book Author', anchor=tk.CENTER, width=400)
    book_list_tree.column('Status', anchor=tk.CENTER, width=100)


    book_list_tree.heading('ID', text='ID')
    book_list_tree.heading('Book Title', text='Book Title')
    book_list_tree.heading('Book Author', text='Book Author')
    book_list_tree.heading('Status', text='Status')

    add_book_list_to_tree(book_list_tree)


    back_button = tk.Button(browse_books_frame, text="Back", font=("Arial", 14), bg="#1A8F2D", fg="white", bd=2, command=lambda:show_frame(user_dashboard_frame))
    back_button.place(x=600, y=800, width=100, height=30)

    book_list_tree.place(x=20, y=350)

    book_list_tree.bind('<<TreeviewSelect>>', lambda event: display_book_details(event, book_list_tree, title_enter, author_enter, isbn_enter, summary_text, shared_data,id_enter))



