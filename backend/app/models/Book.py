# Book resource
class Book:

    # Constructor
    def __init__(self, ISBN, title, edition, publisher) -> None:
        self.ISBN = ISBN
        self.title = title
        self.editiion = edition
        self.publisher = publisher
        # self.topics = list()
        self.topics = ['one', 'two']

    def __str__(self):
        return "ISBN: " + str(self.ISBN) + " Title: " + self.title + " Edition: " + self.editiion + " Publisher: " + self.publisher