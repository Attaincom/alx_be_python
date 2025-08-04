from library_system import Book, EBook, PrintBook, Library

def main():
    library = Library()

    classic_book = Book("Pride and Prejudice", "Jane Austen", 1813)
    digital_book = EBook("Digital Fortress", "Dan Brown", 1998, 512)
    paper_book = PrintBook("The Great Gatsby", "F. Scott Fitzgerald", 1925, 218)

    library.add_book(classic_book)
    library.add_book(digital_book)
    library.add_book(paper_book)

    library.list_books()

if __name__ == "__main__":
    main()
