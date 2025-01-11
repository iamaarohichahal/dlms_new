import sqlite3


class Login:
    def validate_user(self,type_of_user, username, password):
        if type_of_user == 'admin':
            query = 'SELECT * FROM admin WHERE username = ?'
        else: 
            query = 'SELECT * FROM users WHERE username = ?'


        conn = sqlite3.connect('dlms.db')
        cursor = conn.cursor()
        
        cursor.execute(query, (username,))
        user = cursor.fetchone()
        conn.close()

        if user and user[2] == password:  
            return True
        
        else:
           return False
        

