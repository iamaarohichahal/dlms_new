from db_utils import Database
from server.admin_user import Admin_user
from server.normal_user import Normal_user



class Login:
    def validate_user(self,type_of_user, username, password):
        if type_of_user == 'admin':
            user = Admin_user()
        else: 
            user = Normal_user()

        database = Database()
        user = database.fetch_query(user.get_login_query(), (username,))[0]

        if user and user[2] == password:  
            return True
        
        else:
           return False
        

