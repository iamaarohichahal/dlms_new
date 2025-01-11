from db_utils import Database


class Login:
    def validate_user(self,type_of_user, username, password):
        if type_of_user == 'admin':
            query = 'SELECT * FROM admin WHERE username = ?'
        else: 
            query = 'SELECT * FROM users WHERE username = ?'

        database = Database()
        user = database.fetch_query(query, (username,))[0]

        if user and user[2] == password:  
            return True
        
        else:
           return False
        

