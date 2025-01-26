# Base class representation of Books 
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# EBook class inherited from Book 
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = int(file_size)

# PrintBook class also inherited from base class Book 
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = int(page_count)

# class that shows the list of books in the library 
class Library:
    def __init__(self):
        self.books = []


    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)

        else:
            print("Error: only Book, EBook, or PrintBook instances can be added.")


    def list_books(self):
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, {book.file_size}MB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, {book.page_count} pages")
            else:
                print(f"Book: {book.title} by {book.author}")              
