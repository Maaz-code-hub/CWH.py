class Library:
    def __init__(self):
        self.no = 0
        self.books = []

    def addbooks(self):
        book_name = input("Enter the name of the book to be added: ")
        self.books.append(book_name)
        self.no += 1
        print(f'"{book_name}" has been added to the library.')

    def delbooks(self):
        if not self.books:
            print("The library is empty. No books to delete.")
            return
        for i, item in enumerate(self.books):
            print(f"Index: {i+1}, Book: {item}")
        try:
            d = int(input("Enter the index number of the book to be deleted: "))
            removed_book = self.books.pop(d-1)
            self.no -= 1
            print(f'"{removed_book}" has been deleted from the library.')
        except IndexError:
            print("Enter a valid index!")
        except ValueError:
            print("Please enter a valid number.")

    def viewbooks(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("Books in the library:")
            for i, item in enumerate(self.books):
                print(f"Index: {i+1}, Book: {item}")

    def countbooks(self):
        print(f"The count of books in the library is: {self.no}")


# Main Program
library = Library()

while True:
    print("\n===========================================")
    print("Enter your choice:")
    print("1. Add Book\n2. Delete Book\n3. View Books\n4. Count of Books\n5. Exit")
    print("===========================================")
    try:
        choice = int(input())
        if choice == 1:
            library.addbooks()
        elif choice == 2:
            library.delbooks()
        elif choice == 3:
            library.viewbooks()
        elif choice == 4:
            library.countbooks()
        elif choice == 5:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Please enter a valid choice.")
    except ValueError:
        print("Please enter a number.")
