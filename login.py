from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/user_dashboard')
def user_dashboard():
    return render_template('user_dashboard.html')

@app.route('/view_borrowed_books')
def view_borrowed_books():
    return render_template('view_borrowed_books.html')

@app.route('/browse_books')
def browse_books():
    return render_template('browse_books.html')

@app.route('/return_books')
def return_books():
    return render_template('return_books.html')

@app.route('/logout')
def logout():
    # Perform logout operations here
    return render_template('logout.html')

if __name__ == '__main__':
    app.run(debug=True)
