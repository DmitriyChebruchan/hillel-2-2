# Library Management System

This Python-based Library Management System is designed to manage books and magazines efficiently. It incorporates features like iterators, generators, decorators, context managers, and object-oriented programming principles.

## Classes

### Book Model

The `BookModel` class is defined using Pydantic to model book attributes such as title, author, and publication year.

### Book Class

The `Book` class represents a book instance and contains a method to return book information as a string.

### Library Class

The `Library` class manages a collection of books and magazines. It includes:

- Methods to add, remove, and list books in the library.
- Filtering books by author.
- Saving and loading the library contents to/from a file.

## Functionality

- Creating instances of books and magazines.
- Adding and removing items from the library.
- Displaying the library contents.
- Filtering books by author name.
- Saving the library contents to a file and loading them back.

## Usage

1. Create instances of books and magazines using `BookModel`.
2. Add items to the library using `Library.add_book()` or `Library.remove_book()` methods.
3. Use `Library.list_books()` to display all items in the library.
4. Filter books by author with `Library.books_by_author()`.
5. Save the library contents to a file using `Library.save_to_file()` and load them back with `Library.load_from_file()`.

## How to Run

1. Clone this repository.
```
git clone https://github.com/DmitriyChebruchan/hillel-2-2
```
2. Create and activate venv
```
python -m venv myenv
source myenv/bin/activate
```
3. Install the required dependencies from requirements.txt.
```
pip install -r requirements.txt
```
4. Run the script containing the library management system.
```
python script.py
```
