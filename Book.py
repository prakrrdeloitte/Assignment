class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Available books:")
            for book in self.books:
                print(f"Title: {book.title}\tAuthor: {book.author}")


# Creating instances of the Book class
book1 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")

# Creating an instance of the Library class
library = Library()

# Adding books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Displaying available books
library.display_books()

# Removing a book from the library
library.remove_book(book2)

# Displaying available books again
library.display_books()
