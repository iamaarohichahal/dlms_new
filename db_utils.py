# db_utils.py

import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def init_db():
    """
    Initializes the SQLite databases and creates tables if they do not exist.
    """
    # Initialize the users database
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER NOT NULL,
            isbn TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

    # Initialize the admin database
    conn = sqlite3.connect('admin.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS admin(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_user(username, password):
    """
    Inserts a new user into the users table.
    """
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    hashed_password = generate_password_hash(password, method='sha256')
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def fetch_users():
    """
    Fetches all users from the users table.
    """
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, username, password FROM users')
    users = cursor.fetchall()
    conn.close()
    return users

def user_exists(user_id):
    """
    Checks if a user with the given ID exists.
    """
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute('SELECT 1 FROM users WHERE id = ?', (user_id,))
    exists = cursor.fetchone() is not None
    conn.close()
    return exists

def delete_user(user_id):
    """
    Deletes a user with the given ID.
    """
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()

def update_user(user_id, username, password):
    """
    Updates user information.
    """
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    hashed_password = generate_password_hash(password, method='sha256')
    cursor.execute('UPDATE users SET username = ?, password = ? WHERE id = ?', (username, hashed_password, user_id))
    conn.commit()
    conn.close()

def insert_admin(username, password):
    """
    Inserts a new admin into the admin table.
    """
    conn = sqlite3.connect('admin.db')
    cursor = conn.cursor()
    hashed_password = generate_password_hash(password, method='sha256')
    try:
        cursor.execute('INSERT INTO admin (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def fetch_admin(username):
    """
    Fetches admin details by username.
    """
    conn = sqlite3.connect('admin.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, username, password FROM admin WHERE username = ?', (username,))
    admin = cursor.fetchone()
    conn.close()
    return admin

def fetch_user_by_username(username):
    """
    Fetches user details by username.
    """
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, username, password FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    return user

def insert_book(title, author, year, isbn):
    """
    Inserts a new book into the books table.
    """
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books (title, author, year, isbn) VALUES (?, ?, ?, ?)', 
                   (title, author, year, isbn))
    conn.commit()
    conn.close()

def fetch_books():
    """
    Fetches all books from the books table.
    """
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, author, year, isbn FROM books')
    books = cursor.fetchall()
    conn.close()
    return books

def delete_book(book_id):
    """
    Deletes a book with the given ID.
    """
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
    conn.commit()
    conn.close()

def update_book(book_id, title, author, year, isbn):
    """
    Updates book information.
    """
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE books SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?', 
                   (title, author, year, isbn, book_id))
    conn.commit()
    conn.close()
