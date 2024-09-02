# db_utils.py
import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def init_db(self):
        """
        Initializes the SQLite databases and creates tables if they do not exist.
        """
        self.cursor.execute('''
                       CREATE TABLE IF NOT EXISTS users(
                       id INTEGER PRIMARY KEY,
                       username TEXT UNIQUE NOT NULL,
                       password TEXT NOT NULL)
                       ''')
        
        self.cursor.execute('''
                       CREATE TABLE IF NOT EXISTS books(
                       id INTEGER PRIMARY KEY,
                       isbn TEXT UNIQUE NOT NULL,
                       title TEXT NOT NULL,
                       author TEXT NOT NULL,
                       status TEXT NOT NULL)
                       ''')

        self.cursor.execute('''
                       CREATE TABLE IF NOT EXISTS admin(
                       id INTEGER PRIMARY KEY,
                       username TEXT UNIQUE NOT NULL,
                       password TEXT NOT NULL)
                       ''')

        self.conn.commit()

    def fetch_users(self):
        """
        Fetches all users from the 'users' table.
        """
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def insert_user(self, id, username, password):
        """
        Inserts a new user into the 'users' table.
        """
        self.cursor.execute('INSERT INTO users (id, username, password) VALUES (?, ?, ?)',
                            (id, username, password))
        self.conn.commit()

    def close(self):
        """
        Closes the database connection.
        """
        self.conn.close()