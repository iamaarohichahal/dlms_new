from server.user_managment import User



class Admin_user(User):
    def get_login_query(self):
        return 'SELECT * FROM admin WHERE username = ?'
