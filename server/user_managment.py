from db_utils import Database
import sqlite3

class User_management:

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
