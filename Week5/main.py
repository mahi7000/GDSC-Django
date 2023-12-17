class Book:
    def __init__(self, title, author, ISBN, status):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.status = status

    def display(self):
        print(f"Title - {self.title}\nAuthor - {self.author}\nISBN - {self.ISBN}\nAvailability Status - {self.status}")

    def updateStatus(self, status):
        self.status = status

class User:
    def __init__(self, user_id, name, books_borrowed):
        self.user_id = user_id
        self.name = name
        self.books_borrowed = []
    def display(self):
        print(f"Name - {self.name} ({self.user_id})\nBooks borrowed - {self.books_borrowed}")
    def borrow_book(self):
        self.books_borrowed.append(Book[self.name])
    def return_book(self):
        self.books_borrowed.pop(Book[self.name])

class Library:
    def __init__(self, books, user_information):
        self.books = books
        self.user_information = user_information
    def add_books(self):
        self.books.append(Book)
    def add_user(self):
        self.user_information(User)

class Transaction:
    def __init__(self, enter):
        self.enter = enter
    def borrowed(self):
        self.enter -= 1 
    def returned(self):
        self.enter += 1

