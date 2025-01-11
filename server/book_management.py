from db_utils import Database


class Book_management:

    def bubble_sort_titles(self, books):
   
        n = len(books)
            
        # Extract the titles and their associated book data
        for i in range(n):
            for j in range(0, n - i - 1):
                # Compare titles (index 1 is the title)
                if books[j][1].lower() > books[j + 1][1].lower():  
                    books[j], books[j + 1] = books[j + 1], books[j]  # Swap books

        return books
    
    def get_books(self):
        database = Database()
        books = database.fetch_query("SELECT id, title, author, status FROM books")
        

        # Sort the books by title using bubble sort
        return self.bubble_sort_titles(books)

    def get_book(self, book_id):
        database = Database()
        return database.fetch_query("SELECT title, author, isbn, summary FROM books WHERE id=?",(book_id,))[0]

    def search_books(self, search_by_coloumn, search_text):

        query = "SELECT id, title, author, status FROM books WHERE LOWER("+search_by_coloumn+") LIKE ?"

        database = Database()
        return database.fetch_query(query,(f"%{search_text}%",))

    def get_books_2(self):
        database = Database()
        return database.fetch_query("SELECT * FROM books")

    def insert_book(self, id, isbn, Book_title, Book_author ,Book_genre , Book_summary , Book_status):
        database = Database()
        database.execute_query('INSERT INTO books (id, isbn, title, author, genre, summary, status) VALUES (?, ?, ?, ? , ? , ? , ?)',
                                (id, isbn, Book_title, Book_author, Book_genre, Book_summary, Book_status))
    
    def delete_book(self, id):
        database = Database()
        database.execute_query('DELETE FROM books WHERE id = ?', (id,))
    
    def edit_book(self, isbn, book_title, book_author, book_genre, book_summary, book_status, id):
        database = Database()
        database.execute_query("UPDATE books SET isbn = ?, title = ? , author = ?, genre = ?, summary= ?, status= ? WHERE id = ?", 
                        (isbn,book_title, book_author, book_genre,book_summary, book_status, id))
