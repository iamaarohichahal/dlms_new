from db_utils import Database
from datetime import datetime, timedelta


class Loan_management:
    def get_loans(self,user_id):
        database = Database()

        return database.fetch_query(''' 
                SELECT b.book_id, bo.title, bo.author, bo.genre, b.return_date
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

                    database.execute_query(
                        'DELETE FROM borrowed_books WHERE book_id = ? AND user_id = ?',
                        (book_id, user_id)
                    )
                    return True
        else:
              return False 

    def borrow_book(self, user_id, book_id):
        database = Database()
        

        borrow_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return_date = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d %H:%M:%S')


        database.execute_query('''
            INSERT INTO borrowed_books (book_id, user_id, borrow_date, return_date, status)
            VALUES (?, ?, ?, ?, ?)
        ''', (book_id, user_id, borrow_date, return_date, 'borrowed'))


        database.execute_query('''
            UPDATE books
            SET status = 'borrowed'
            WHERE id = ?
        ''', (book_id,))

        return True

    def check_and_update_overdue_books(self):
        database = Database()
        current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

  
        database.execute_query('''
            UPDATE borrowed_books
            SET status = 'overdue'
            WHERE return_date < ? AND status = 'borrowed'
        ''', (current_datetime,))
        
    def get_loans_2(self):
        database = Database()

        return database.fetch_query(''' 
     SELECT b.book_id, b.user_id, bo.title, b.return_date, b.status
    FROM borrowed_books b
    JOIN books bo ON b.book_id = bo.id
    ''')
    
    def get_overdue_books(self, user_id):
        database = Database()  
        query = '''
        SELECT b.book_id, bo.title
        FROM borrowed_books b
        JOIN books bo ON b.book_id = bo.id
        WHERE b.user_id = ? AND b.status = 'overdue'
        '''
        return database.fetch_query(query, (user_id,))

            

