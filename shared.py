class Shared:
    def __init__(self):
        self._userId = "" 
        self.selected_book = None  # Add selected_book attribute to store selected book details

    def get_user_id(self):
        return self._userId

    def set_user_id(self, value):
        print("set user:" + value)
        if isinstance(value, str) and value:
            self._userId = value
        else:
            raise ValueError("Name must be a non-empty string")

    def set_selected_book(self, book_details):
        if isinstance(book_details, dict) and "title" in book_details and "author" in book_details and "isbn" in book_details:
            self.selected_book = book_details
        else:
            raise ValueError("Selected book must be a dictionary with 'title', 'author', and 'isbn' keys")

    def get_selected_book(self):
        return self.selected_book