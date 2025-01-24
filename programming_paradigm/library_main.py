import unittest
from library_management import Book, Library  # Import both Book and Library

class TestLibraryManagement(unittest.TestCase):
    def setUp(self):
        # Set up the library and add some Nigerian books
        self.library = Library()
        self.library.add_book("Things Fall Apart", "Chinua Achebe")
        self.library.add_book("Half of a Yellow Sun", "Chimamanda Ngozi Adichie")
        self.library.add_book("The Famished Road", "Ben Okri")

    def test_add_book(self):
        # Add another book and verify it exists
        self.library.add_book("Sozaboy", "Ken Saro-Wiwa")
        books = self.library.list_available_books()
        self.assertIn("Sozaboy by Ken Saro-Wiwa", books)

    def test_check_out_book(self):
        # Check out a book and verify it's no longer available
        message = self.library.check_out_book("Things Fall Apart")
        self.assertEqual(message, "'Things Fall Apart' has been checked out.")
        books = self.library.list_available_books()
        self.assertNotIn("Things Fall Apart by Chinua Achebe", books)

        # Attempt to check out the same book again
        message = self.library.check_out_book("Things Fall Apart")
        self.assertEqual(message, "'Things Fall Apart' is not available.")

    def test_return_book(self):
        # Check out a book, then return it
        self.library.check_out_book("Half of a Yellow Sun")
        message = self.library.return_book("Half of a Yellow Sun")
        self.assertEqual(message, "'Half of a Yellow Sun' has been returned.")
        books = self.library.list_available_books()
        self.assertIn("Half of a Yellow Sun by Chimamanda Ngozi Adichie", books)

        # Attempt to return a book that isn't checked out
        message = self.library.return_book("Half of a Yellow Sun")
        self.assertEqual(message, "'Half of a Yellow Sun' was not checked out.")

    def test_list_available_books(self):
        # Check availability after checkout
        self.library.check_out_book("The Famished Road")
        books = self.library.list_available_books()
        self.assertIn("Things Fall Apart by Chinua Achebe", books)
        self.assertIn("Half of a Yellow Sun by Chimamanda Ngozi Adichie", books)
        self.assertNotIn("The Famished Road by Ben Okri", books)


if __name__ == "__main__":
    unittest.main()
