from issues_classes import Magazine, BookModel
from library_classes import BookLibrary, MagazineLibrary

# Creating instances of books and magazines
book1 = BookModel(title="The Catcher in the Rye", author="J.D. Salinger", year=1951)
book2 = BookModel(title="To Kill a Mockingbird", author="Harper Lee", year=1960)
magazine1 = Magazine(title="Magazine A", author="Mag Author", year=2022)

# Creating a BookLibrary and MagazineLibrary
book_library = BookLibrary()
magazine_library = MagazineLibrary()

# Adding books and magazines to their respective libraries
book_library.add_book(book1)
book_library.add_book(book2)
magazine_library.add_book(magazine1)

# Displaying all books in the BookLibrary
print("List of all books in BookLibrary:")
book_library.list_books()

# Displaying all magazines in the MagazineLibrary
print("\nList of all magazines in MagazineLibrary:")
magazine_library.list_books()

# Displaying books by a specific author in BookLibrary
print("\nBooks by author 'Harper Lee' in BookLibrary:")
book_library.books_by_author('Harper Lee')

# Saving BookLibrary contents to a file
book_library.save_to_file('books.txt')

# Removing a book from BookLibrary
book_library.remove_book(book1)

# Displaying books after removal in BookLibrary
print("\nBooks after removal in BookLibrary:")
book_library.list_books()

# Loading books from a file to BookLibrary and displaying them
book_library.load_from_file('books.txt')
print("\nBooks after loading from file in BookLibrary:")
book_library.list_books()

# Saving MagazineLibrary contents to a file
magazine_library.save_to_file('magazines.txt')

# Removing a magazine from MagazineLibrary
magazine_library.remove_book(magazine1)

# Displaying magazines after removal in MagazineLibrary
print("\nMagazines after removal in MagazineLibrary:")
magazine_library.list_books()

# Loading magazines from a file to MagazineLibra
magazine_library.load_from_file('magazines.txt')
print("\nMagazines after loading from file in MagazineLibrary:")
magazine_library.list_books()