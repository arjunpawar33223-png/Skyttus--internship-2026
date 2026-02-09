class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: {self.price}")

# Example
book = Book("Python Basics", "John Doe", 299)
book.display_details()