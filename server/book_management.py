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

    
    def borrow_book(self,user_id,book_id):
        db = Database()
        from datetime import datetime, timedelta
        
        # Get the current date and calculate the return date
        borrow_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return_date = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d %H:%M:%S')

        # Insert the borrowing record into the borrowed_books table
        db.execute_query('''
            INSERT INTO borrowed_books (book_id, user_id, borrow_date, return_date, status)
            VALUES (?, ?, ?, ?, ?)
        ''', (book_id, user_id, borrow_date, return_date, 'borrowed'))

        # Update the status of the book in the books table
        db.execute_query('''
            UPDATE books
            SET status = 'borrowed'
            WHERE id = ?
        ''', (book_id,))

        db.execute_query('UPDATE books SET status = "borrowed" WHERE id = ?', (book_id,))
        return True

    