class Shared:
    def __init__(self):
        self._userId = "" 

    def get_user_id(self):
        return self._userId

    def set_user_id(self, value):
        print("set user:" + value)
        if isinstance(value, str) and value:
            self._userId = value
        else:
            raise ValueError("Name must be a non-empty string")

