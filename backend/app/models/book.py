# Book resource
class Book:

    # Constructor
    def __init__(self, ISBN, title, edition, publisher) -> None:
        self.ISBN = ISBN
        self.title = title
        self.editiion = edition
        self.publisher = publisher