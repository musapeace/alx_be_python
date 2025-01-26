from book_class import Book

def main():
    my_book = Book(1984, "George Orwell", 1949)

# str method illustration 
    print(my_book)


# repr method print example 
    print(repr(my_book))

# deleting a book instance 
    del my_book

if __name__ == "__main__":
    main()