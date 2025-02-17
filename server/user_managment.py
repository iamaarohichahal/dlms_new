from db_utils import Database
import sqlite3

class User:
    def get_login_query(self):
        return ""
    
    def register_user(self,type_of_user, username, password):
        if type_of_user == 'admin':
            query = 'INSERT INTO admin (username, password) VALUES (?, ?)'
        else: 
            query = 'INSERT INTO users (username, password) VALUES (?, ?)'

        status = 'true'
        database = Database()
        
        try:
            database.execute_query(query, (username, password))
          
        except sqlite3.IntegrityError:
            status = 'false'

        return status

    def get_users(self):
        database = Database()
        return database.fetch_query("SELECT * FROM users")
    
    def insert_user(self,id,username,password):
        database = Database()

        database.execute_query('INSERT INTO users (id, username, password) VALUES (?, ?, ?)',(id, username, password))

    def delete_user(self,id):
         database = Database()
         database.execute_query('DELETE FROM users WHERE id = ?', (id,))

    def edit_user(self,id,username,password):
         database = Database()
         database.execute_query("UPDATE users SET username = ?, password = ? WHERE id = ?", 
                    (username, password, id))