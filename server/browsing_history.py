


class Browsing_history_stack: 
    def __init__(self):
        self.browsing_history = []

    def isEmpty(self):
        return self.browsing_history == []
    
    def push(self,books):
        self.browsing_history.append(books)

    def get_browsing_history(self):
        for browsing_history in reversed(self.browsing_history):
            print(browsing_history)

         