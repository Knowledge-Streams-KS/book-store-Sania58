class Books:
    def __init__(self, title, author, genre, price, quantity):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.quantity = quantity

class Bookstore:
    books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"{title} has been removed from the inventory.")
                return
        print(f"Book with title '{title}' not found in the inventory.")

    def search_by_title(self, title):
        found_books = [book for book in self.books if book.title.lower() == title.lower()]
        if found_books:
            for book in found_books:
                print(f"Title of book {book.title}, quantity is this {book.quantity} , price of book {book.price}, author of book is {book.author} and type is this"
                      f" {book.genre}")
        else:
            print(f"No books found with title '{title}'.")

    def search_by_author(self, author):
        found_books = [book for book in self.books if book.author.lower() == author.lower()]
        if found_books:
            for book in found_books:
                print(
                    f"Author of book is {book.author} , andTitle of book {book.title}, quantity is this {book.quantity} , price of book {book.price}, and type is this"
                    f" {book.genre}")
        else:
            print(f"No books found by author '{author}'.")

    def display_books(self):
        if self.books:
            for book in self.books:
                print(
                    f"Author of book is {book.author} , andTitle of book {book.title}, quantity is this {book.quantity} , price of book {book.price}, and type is this"
                    f" {book.genre}")
        else:
            print("No books in the inventory.")

    def buy_book(self, user):
        title = input("Enter the title of the book you want to buy: ")
        for book in self.books:
            if book.title.lower() == title.lower():
                quantity_to_buy = int(input("Enter the quantity you want to buy: "))
                if quantity_to_buy <= book.quantity:
                    book.quantity -= quantity_to_buy
                    user.book_collection.append(book)
                    print(f"You have successfully purchased {quantity_to_buy} book of {book.title}.")
                    return
                else:
                    print(f"Sorry, only {book.quantity} book of {book.title} are available.")
                    return
        print(f"Book with title '{title}' not found in the inventory.")

class User:
    def _init_(self, name, age, address, book_collection=None):
        self.name = name
        self.age = age
        self.address = address
        if book_collection is None:
            book_collection = []
        self.book_collection = book_collection

    def display_books_collection(self):
        if self.book_collection:
            for book in self.book_collection:
                print(f"Your collected book's title is {book.title} and type is this"
                      f" {book.genre}")
        else:
            print("Your books collection is empty.")

# Sample code to run the program

bookstore = Bookstore()
user = None

while True:
    print("\nWelcome to the Online Bookstore")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search by title")
    print("4. Search by author")
    print("5. Display all books")
    print("6. Buy a book")
    print("7. Display user's books collection")
    print("8. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        genre = input("Enter the genre of the book: ")
        price = float(input("Enter the price of the book: "))
        quantity = int(input("Enter the quantity of the book: "))
        new_book = Books(title, author, genre, price, quantity)
        bookstore.add_book(new_book)

    elif choice == '2':
        title = input("Enter the title of the book to remove: ")
        bookstore.remove_book(title)

    elif choice == '3':
        title = input("Enter the title to search: ")
        bookstore.search_by_title(title)

    elif choice == '4':
        author = input("Enter the author to search: ")
        bookstore.search_by_author(author)

    elif choice == '5':
        bookstore.display_books()

    elif choice == '6':
        user_name = input("Enter your name: ")
        user_age = input("Enter your age: ")
        user_address = input("Enter your address: ")
        user = User(user_name, user_age, user_address)
        bookstore.buy_book(user)

    elif choice == '7':
        if user != None:
            user.display_books_collection()
        else:
            print("Not Found any collection")

    elif choice == '8':
        print("Thank you for using the Online Bookstore. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1-8.")