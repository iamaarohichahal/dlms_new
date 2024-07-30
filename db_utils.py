import sqlite3

# Initialize the database
def init_db():
    """
    Initializes the SQLite databases and creates tables if they do not exist.
    """
    # Initialize the users database
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS users(
                   id INTEGER PRIMARY KEY,
                   username TEXT UNIQUE NOT NULL,
                   password TEXT NOT NULL)
                   ''')
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS books(
                   id INTEGER PRIMARY KEY,
                   title TEXT NOT NULL,
                   author TEXT NOT NULL,
                   year INTEGER NOT NULL,
                   isbn TEXT NOT NULL)
                   ''')
    conn.commit()
    conn.close()

    # Initialize the admin database
    conn = sqlite3.connect('admin.db')
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS admin(
                   id INTEGER PRIMARY KEY,
                   username TEXT UNIQUE NOT NULL,
                   password TEXT NOT NULL)
                   ''')
    conn.commit()
    conn.close()