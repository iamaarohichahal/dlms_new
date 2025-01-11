from db_utils import Database, DB_NAME
import sqlite3




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
        books = database.fetch_book_list()

        # Sort the books by title using bubble sort
        return self.bubble_sort_titles(books)

    def get_book(self, book_id):
        conn = sqlite3.connect(DB_NAME) 
        cursor = conn.cursor()
        
        cursor.execute("SELECT title, author, isbn, summary FROM books WHERE id=?", (book_id,))
        return cursor.fetchone()

    def search_books(self, search_by_coloumn, search_text):

        query = "SELECT id, title, author, status FROM books WHERE LOWER("+search_by_coloumn+") LIKE ?"

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Use SQL LIKE operator to perform a case-insensitive search
        cursor.execute(query, (f"%{search_text}%",))
        filtered_books = cursor.fetchall()
        conn.close()
        return filtered_books

        