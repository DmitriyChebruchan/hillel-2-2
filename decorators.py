import functools


def log_addition(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Adding book: {args[1]} by {args[2]}")
        return func(*args, **kwargs)

    return wrapper


def check_book_existence(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if args[1] in args[0].books:
            return func(*args, **kwargs)
        print("Book not found in the library.")

    return wrapper
