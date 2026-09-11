class Hotel:
    def __init__(self):
        self.customer_id = 0
        self.name = ""
        self.bill = 0

    def add_customer(self):
        self.customer_id = int(input("Enter the customer id: "))
        self.name = input("Enter the customer name: ")
        print("Customer added successfully....!")

    def book_room(self):
        self.bill = float(input("Enter the room charge: "))
        print("Room booked successfully....!")

    def check_out(self):
        print("Check out completed successfully....!")

    def bill_enquiry(self):
        print("Bill Amount:", self.bill)

    def customer_details(self):
        print("........Customer Details........")
        print("Customer ID:", self.customer_id)
        print("Customer Name:", self.name)
        print("Bill Amount:", self.bill)


obj = Hotel()
while True:
    print("1.Add Customer")
    print("2.Book Room")
    print("3.Check Out")
    print("4.Bill Enquiry")
    print("5.Customer Details")
    print("6.Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        obj.add_customer()
    elif choice == 2:
        obj.book_room()
    elif choice == 3:
        obj.check_out()
    elif choice == 4:
        obj.bill_enquiry()
    elif choice == 5:
        obj.customer_details()
    elif choice == 6:
        print("Thank You....")
        break
    else:
        print("Invalid Choice")