from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Initialize the database
def init_db():
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS Admin_KPSTR(
                   id INTEGER PRIMARY KEY,
                   username TEXT UNIQUE NOT NULL,
                   password TEXT NOT NULL)
                   ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('user.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Admin_KPSTR WHERE username = ?', (username,))
        user = cursor.fetchone()
        conn.close()
        
        if user and check_password_hash(user[2], password):
            session['user_id'] = user[0]
            session['username'] = user[1]
            return redirect(url_for('user_dashboard'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')
        
        conn = sqlite3.connect('user.db')
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO Admin_KPSTR (username, password) VALUES (?, ?)', (username, hashed_password))
            conn.commit()
            flash('Registration successful! Please log in.')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username already exists')
        conn.close()
    return render_template('register.html')

@app.route('/user_dashboard')
def user_dashboard():
    if 'username' in session:
        return render_template('user_dashboard.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/view_borrowed_books')
def view_borrowed_books():
    if 'username' in session:
        return render_template('view_borrowed_books.html')
    return redirect(url_for('login'))

@app.route('/browse_books')
def browse_books():
    if 'username' in session:
        return render_template('browse_books.html')
    return redirect(url_for('login'))

@app.route('/return_books')
def return_books():
    if 'username' in session:
        return render_template('return_books.html')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    flash('You have been logged out.')
    return redirect(url_for('login'))

@app.route('/view_book_details/<int:book_id>')
def view_book_details(book_id):
    if 'username' in session:
        return render_template('view_book_details.html', book_id=book_id)
    return redirect(url_for('login'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
