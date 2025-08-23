class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book.title} by {book.author}")
    def remove_book(self, book):
        self.books.remove(book)
        print(f"Book removed: {book.title} by {book.author}")
    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                print(f"Book found: {book.title} by {book.author}")
                return True
        print("Book not found")
        return False
    
Book1=Book("The Great Gatsby", "F. Scott Fitzgerald")
Book2=Book("1984", "George Orwell")
Book3=Book("To Kill a Mockingbird", "Harper Lee")


Library=Library()
Library.add_book(Book1)
Library.add_book(Book2)
Library.add_book(Book3)
Library.search_book("The Great Gatsby")
Library.search_book("1984")
Library.remove_book(Book1)
Library.search_book("The Great Gatsby")
Library.search_book("To Kill a Mockingbird")







