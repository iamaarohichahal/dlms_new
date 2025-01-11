# db_utils.py
import sqlite3
DB_NAME = "dlms.db"
class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.cursor = self.conn.cursor()

    def init_db(self):
       
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
       
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def get_all_books_as_array(self):
       
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
       
        self.cursor.execute("SELECT * FROM books")
        return self.cursor.fetchall()
 
    def insert_book(self,id, isbn, book_title, book_author, book_genre, book_summary, book_status):
            
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
    
    def execute_query(self, query, params=None):
        """
        Execute a query that doesn't return results (e.g., INSERT, UPDATE, DELETE).
        
        :param query: The SQL query to execute.
        :param params: Optional tuple of parameters to pass into the query.
        """
        try:
            if not self.conn:
                raise ConnectionError("Database not connected.")
            self.cursor.execute(query, params or ())
            self.conn.commit()
            print("Query executed successfully.")
        except sqlite3.Error as e:
            self.conn.rollback()
            print(f"Error executing query: {e}")
            raise

    def fetch_query(self, query, params=None):
        """
        Execute a query that fetches results (e.g., SELECT).
        
        :param query: The SQL query to execute.
        :param params: Optional tuple of parameters to pass into the query.
        :return: List of tuples containing the query results.
        """
        try:
            if not self.conn:
                raise ConnectionError("Database not connected.")
            self.cursor.execute(query, params or ())
            results = self.cursor.fetchall()
            print("Query executed successfully. Results fetched.")
            return results
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
            raise

    # Call the function to test
    if __name__ == "__main__":
        get_all_books_as_array()


    

    def close(self):
            """
            Closes the database connection.
            """
            self.conn.close()


    