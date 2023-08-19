class Library:
    def __init__(self, listofBooks):
        self.books = listofBooks

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books:
            print(" *" + book)

    def borrowBooks(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}.")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book is not available.")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book.")


class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow:")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return:")
        return self.book


if __name__ == "__main__":
    centralLibrary = Library(
        ["Algorithm", "Data structure", "Python", "Operating system"])
    student = Student()
    # centralLibrary.displayAvailableBooks()

    while(True):
        welcomemg = ''' ****Welcome to Central Library****
        Please choose an option:
        1. List of all books
        2. Request a book
        3. Return a book
        4. Exit the library
        '''
        print(welcomemg)
        a = int(input("Enter a choice:"))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBooks(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks fo visiting our library.")
            exit()
        else:
            print("wrong choice")
