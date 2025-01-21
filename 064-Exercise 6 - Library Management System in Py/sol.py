class Library:
    no=0
    books = []

lib=Library()
def addbooks():
        a=input("Enter the name of the book to be added :")
        lib.books.append(a)
        lib.no+=1

def delbooks():
        for i, item in enumerate(lib.books):
            print(f"Index: {i+1}, Book: {item}")
        try:
            d=int(input("Enter the index no of the to be deleted :"))
            lib.books.pop(d-1)
            lib.no-=1
        except IndexError:
            print("Enter a valid index!!!")


def viewbooks():
    if not lib.books:
        print("The library is empty.")
    else:
        print("Books in the library:")
        for i, item in enumerate(lib.books):
            print(f"Index: {i + 1}, Book: {item}")
    

while(True):
    print("===========================================")
    print("Enter the choice")
    print("1.Add Book\n2.Delete Book\n3.View Books\n4.Count of books\n5.Exit")
    print("===========================================")
    c=int(input())
    if c==1:
        addbooks()
    elif c==2:
        delbooks()
    elif c==3:
        viewbooks()
    elif c==4:
        print(f"The count of books in library are {lib.no}")
        print(f"The count of books in library are {len(lib.books)}")
    elif c==5:
        exit()
    

