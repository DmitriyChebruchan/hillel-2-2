from decorators import log_addition, check_book_existence
from abc import ABC, abstractmethod
from issues_classes import BookModel


class Library(ABC):
    def __init__(self):
        self.books = []

    def list_books(self):
        # Display all books in the library
        for book in self.books:
            print(book)

    def books_by_author(self, author):
        # Display books by a specific author
        for book in self.books:
            if book.author == author:
                print(book)

    def __iter__(self):
        return iter(self.books)

    def books_by_author_generator(self, author):
        # Generate books by a specific author
        for book in self.books:
            if book.author == author:
                yield book

    # Context management commands
    def save_to_file(self, filename):
        # Save library content to a file
        with open(filename, "w") as file:
            for book in self.books:
                file.write(f"{book.title},{book.author},{book.year}\n")

    def load_from_file(self, filename):
        # Load library content from a file
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                book_info = line.strip().split(",")
                book = BookModel(
                    title=book_info[0],
                    author=book_info[1],
                    year=int(book_info[2]),
                )
                self.add_book(book)

    def count_books_by_year(self, year):
        # Count books published in a specific year
        count = len([item for item in self.books if item.year == year])
        print(f"Number of books published in {year}: {count}")

    @abstractmethod
    def add_book(self, book):
        pass

    @abstractmethod
    def remove_book(self, book):
        pass


class BookLibrary(Library):
    @log_addition
    def add_book(self, book):
        # Add a book to the library with logging
        self.books.append(book)

    @check_book_existence
    def remove_book(self, book):
        # Remove a book from the library with existence check
        self.books.remove(book)


class MagazineLibrary(Library):
    @log_addition
    def add_book(self, magazine):
        # Add a magazine to the library with logging
        self.books.append(magazine)

    @check_book_existence
    def remove_book(self, magazine):
        # Remove a magazine from the library with existence check
        self.books.remove(magazine)
