class Movie:
    def __init__(self):
        self.customer_id = 0
        self.name = ""
        self.tickets = 0

    def add_customer(self):
        self.customer_id = int(input("Enter the customer id: "))
        self.name = input("Enter the customer name: ")
        print("Customer added successfully....!")

    def book_ticket(self):
        self.tickets = int(input("Enter the number of tickets: "))
        print("Ticket booked successfully....!")

    def cancel_ticket(self):
        self.tickets = 0
        print("Ticket cancelled successfully....!")

    def booking_details(self):
        print("........Booking Details........")
        print("Customer ID:", self.customer_id)
        print("Customer Name:", self.name)
        print("Tickets Booked:", self.tickets)


obj = Movie()
while True:
    print("1.Add Customer")
    print("2.Book Ticket")
    print("3.Cancel Ticket")
    print("4.Booking Details")
    print("5.Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        obj.add_customer()
    elif choice == 2:
        obj.book_ticket()
    elif choice == 3:
        obj.cancel_ticket()
    elif choice == 4:
        obj.booking_details()
    elif choice == 5:
        print("Thank You for choosing us....")
        break
    else:
        print("Invalid Choice")