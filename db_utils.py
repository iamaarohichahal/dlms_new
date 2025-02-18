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
        
        self.cursor.execute('PRAGMA foreign_keys = ON;')

        #borrowed_books table
        self.cursor.execute('''
                        CREATE TABLE IF NOT EXISTS borrowed_books (
                            book_id INTEGER NOT NULL,
                            user_id INTEGER NOT NULL,
                            borrow_date TEXT NOT NULL,
                            return_date TEXT NOT NULL,
                            status TEXT ,
                            PRIMARY KEY (book_id, user_id),
                            FOREIGN KEY (book_id) REFERENCES books(id),
                            FOREIGN KEY (user_id) REFERENCES users(id)
                        )
                    ''')


        self.conn.commit()
    

    
    def execute_query(self, query, params=None):
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
    

    def close(self):
            self.conn.close()


    