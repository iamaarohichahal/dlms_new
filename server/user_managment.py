import sqlite3
from db_utils import DB_NAME


class User_management:

    def register_user(self,type_of_user, username, password):
        if type_of_user == 'admin':
            query = 'INSERT INTO admin (username, password) VALUES (?, ?)'
        else: 
            query = 'INSERT INTO users (username, password) VALUES (?, ?)'

        status = 'true'
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        try:
    
            cursor.execute(query, (username, password))
            conn.commit()
          
        except sqlite3.IntegrityError:
            status = 'false'
        conn.close()
        return status
