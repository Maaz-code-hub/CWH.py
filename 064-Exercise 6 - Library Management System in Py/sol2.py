class library:
    def __init__(self):
        self.books=[]
        self.no_of_books=0

    def add_book(self):
        new_book=input("enter th book name to be added :")
        self.books.append(new_book)
        self.no_of_books+=1
        print(f"The book {new_book} added succesfully")

    def view_books(self):
        if not self.books:
            print("lib is empty")
        for i,book in enumerate(self.books,start=1):
            print(f"Book Address {i} : Book Name {book}")

    def del_book(self):
        self.view_books()
        indx_of_book=int(input("Enter the Address of book to be deleted : "))
        self.books.pop(indx_of_book-1)


#main prog
lib=library()
while True:
    print("**********************************************************")
    print("Chose from the below options :")
    print("0.Exit\n1.Add Book\n2.View Books\n3.Delete book")
    print("**********************************************************")
    opt=int(input())
    match opt:
        case 0:exit()
        case 1:lib.add_book()
        case 2:lib.view_books()
        case 3:lib.del_book()
