from db_utils import Database


class Loan_management:
    def get_loans(self,user_id):
        database = Database()

        return database.fetch_query(''' 
                SELECT b.book_id, bo.isbn, bo.title, bo.author, bo.genre, bo.summary, b.return_date
                FROM borrowed_books b
                JOIN books bo ON b.book_id = bo.id
                WHERE b.user_id = ?''', (user_id,))
    
    def return_borrowed_book(self,book_id,user_id):
        database = Database()
        borrowed_book= database.fetch_query(
                    'SELECT * FROM borrowed_books WHERE book_id = ? AND user_id = ?',
                    (book_id, user_id)
                )
        if borrowed_book:
                    # Remove the book from the borrowed_books table
                    database.execute_query(
                        'DELETE FROM borrowed_books WHERE book_id = ? AND user_id = ?',
                        (book_id, user_id)
                    )
                    return True
        else:
              return False 

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