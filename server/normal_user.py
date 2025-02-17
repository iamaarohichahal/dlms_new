from server.user_managment import User


class Normal_user(User):
    def get_login_query(self):
        return "SELECT * FROM users WHERE username = ?"
