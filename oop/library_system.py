class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"

class EBook(Book):
    def __init__(self, title, author, publication_year, file_size):
        super().__init__(title, author, publication_year)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {super().__str__()}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title, author, publication_year, page_count):
        super().__init__(title, author, publication_year)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {super().__str__()}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)  # This will automatically call the __str__ method
