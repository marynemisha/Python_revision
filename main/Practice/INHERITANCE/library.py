class Library:
    def __init__(self):
        self.book_id = 0
        self.book_name = ""
        self.available = 0

    def add_book(self):
        self.book_id = int(input("Enter the book id: "))
        self.book_name = input("Enter the book name: ")
        self.available = int(input("Enter the number of books: "))
        print("Book added successfully....!")

    def issue_book(self):
        if self.available > 0:
            self.available -= 1
            print("Book issued successfully....!")
        else:
            print("Book not available....!")

    def return_book(self):
        self.available += 1
        print("Book returned successfully....!")

    def book_details(self):
        print("........Book Details........")
        print("Book ID:", self.book_id)
        print("Book Name:", self.book_name)
        print("Available Books:", self.available)

    def available_books(self):
        print("Available Books:", self.available)


obj = Library()

while True:
    print("1.Add Book")
    print("2.Issue Book")
    print("3.Return Book")
    print("4.Book Details")
    print("5.Available Books")
    print("6.Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        obj.add_book()
    elif choice == 2:
        obj.issue_book()
    elif choice == 3:
        obj.return_book()
    elif choice == 4:
        obj.book_details()
    elif choice == 5:
        obj.available_books()
    elif choice == 6:
        print("Thank You....")
        break
    else:
        print("Invalid Choice")