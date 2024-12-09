# db_utils.py
import sqlite3
from datetime import datetime,timedelta
from tkinter import messagebox
DB_NAME = "dlms.db"
class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.cursor = self.conn.cursor()

    def init_db(self):
        """
        Initializes the SQLite databases and creates tables if they do not exist.
        """
        # Users Table
        self.cursor.execute('''
                       CREATE TABLE IF NOT EXISTS users(
                       id INTEGER PRIMARY KEY,
                       username TEXT UNIQUE NOT NULL,
                       password TEXT NOT NULL)
                       ''')

        # Books Table
        self.cursor.execute('''
                       CREATE TABLE IF NOT EXISTS books(
                        id INTEGER PRIMARY KEY,
                        isbn TEXT NOT NULL,  
                        title TEXT NOT NULL,
                        author TEXT NOT NULL,
                        genre TEXT NOT NULL,
                        summary TEXT NOT NULL,
                        status TEXT NOT NULL)
                       ''')


        # Admin Table
        self.cursor.execute('''
                       CREATE TABLE IF NOT EXISTS admin(
                       id INTEGER PRIMARY KEY,
                       username TEXT UNIQUE NOT NULL,
                       password TEXT NOT NULL)
                       ''')
        # Enable foreign key constraints in SQLite
        self.cursor.execute('PRAGMA foreign_keys = ON;')

        # Create the borrowed_books table
        self.cursor.execute('''
                        CREATE TABLE IF NOT EXISTS borrowed_books (
                            book_id INTEGER NOT NULL,
                            user_id INTEGER NOT NULL,
                            borrow_date TEXT NOT NULL,
                            return_date TEXT NOT NULL,
                            status TEXT DEFAULT 'borrowed',
                            PRIMARY KEY (book_id, user_id),
                            FOREIGN KEY (book_id) REFERENCES books(id),
                            FOREIGN KEY (user_id) REFERENCES users(id)
                        )
                    ''')


        self.conn.commit()

        
    def fetch_users(self):
        """
        Fetches all users from the 'users' table.
        """
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def get_all_books_as_array(self):
        """
        Fetches all books from the database and returns them in a simple list/array.
        Only includes: title, author, status.
        """
        self.cursor.execute("SELECT title, author, status FROM books")
        books_array = self.cursor.fetchall()
        return books_array
    

    def insert_user(self, id, username, password):
        """
        Inserts a new user into the 'users' table.
        """
        self.cursor.execute('INSERT INTO users (id, username, password) VALUES (?, ?, ?)',
                            (id, username, password))
        self.conn.commit()


    def delete_user(id):
        conn =sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM users WHERE id = ?', (id,))
        conn.commit()
        conn.close()

    def update_user(new_username, new_password, id):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("UPDATE users SET username = ?, password = ? WHERE id = ?", 
                    (new_username, new_password, id))
        
        conn.commit()
        conn.close()

    def fetch_books(self):
        """
        Fetches all books from the 'books' table.
        """
        self.cursor.execute("SELECT * FROM books")
        return self.cursor.fetchall()
 

    def insert_book(self,id, isbn, book_title, book_author, book_genre, book_summary, book_status):
            """
            Inserts a new  book into the 'books' table.
            """
            self.cursor.execute('INSERT INTO books (id, isbn, title, author, genre, summary, status) VALUES (?, ?, ?, ? , ? , ? , ?)',
                                (id, isbn, book_title, book_author, book_genre, book_summary, book_status))
            self.conn.commit()

    def delete_book(id):
        conn =sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM books WHERE id = ?', (id,))
        conn.commit()
        conn.close()

    def update_book(new_isbn, new_title, new_author, new_genre, new_summary, new_status, id):
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()

            cursor.execute("UPDATE books SET isbn = ?, title = ? , author = ?, genre = ?, summary= ?, status= ? WHERE id = ?", 
                        (new_isbn, new_title, new_author, new_genre, new_summary, new_status, id))
            
            conn.commit()
            conn.close()

    def fetch_book_list(self):
        """
        Fetches book title, author, and status from the 'books' table.
        """
        self.cursor.execute("SELECT id, title, author, status FROM books")
        return self.cursor.fetchall()
    
    def borrow_book(self, book_id, user_id):
        """
        Inserts a record into the borrowed_books table when a user borrows a book
        and updates the status of the book in the books table to 'borrowed'.
        """
        from datetime import datetime, timedelta
        
        # Get the current date and calculate the return date
        borrow_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return_date = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d %H:%M:%S')

        # Insert the borrowing record into the borrowed_books table
        self.cursor.execute('''
            INSERT INTO borrowed_books (book_id, user_id, borrow_date, return_date, status)
            VALUES (?, ?, ?, ?, ?)
        ''', (book_id, user_id, borrow_date, return_date, 'borrowed'))

        # Update the status of the book in the books table
        self.cursor.execute('''
            UPDATE books
            SET status = 'borrowed'
            WHERE id = ?
        ''', (book_id,))

        # Commit the changes to the database
        self.conn.commit()

    def fetch_borrowed_books_by_user(self, user_id):
        self.cursor.execute('''
            SELECT b.id, b.isbn, b.title, b.author, b.genre, b.summary, bb.return_date, bb.status
            FROM borrowed_books bb
            INNER JOIN books b ON bb.book_id = b.id
            WHERE bb.user_id = ?
        ''', (user_id,))
        return self.cursor.fetchall()
    

    def get_all_books_as_array(self):
       
        
        db = Database()

        # Fetch books from the database
        books_array = db.get_all_books_as_array()


        # Bubble sort to sort by title (case-insensitive)
        n = len(books_array)
        for i in range(n):
            for j in range(0, n - i - 1):
                if books_array[j][0].lower() > books_array[j + 1][0].lower():
                    books_array[j], books_array[j + 1] = books_array[j + 1], books_array[j]

        # Print sorted books
        print("Sorted Books Array:")
        for book in books_array:
            print(book)

        return books_array

    # Call the function to test
    if __name__ == "__main__":
        get_all_books_as_array()


    

    def close(self):
            """
            Closes the database connection.
            """
            self.conn.close()


    