class Bus:
    def __init__(self):
        self.passenger_id = 0
        self.name = ""
        self.ticket = False

    def add_passenger(self):
        self.passenger_id = int(input("Enter the passenger id: "))
        self.name = input("Enter the passenger name: ")
        print("Passenger added successfully....!")

    def book_ticket(self):
        self.ticket = True
        print("Ticket booked successfully....!")

    def cancel_ticket(self):
        self.ticket = False
        print("Ticket cancelled successfully....!")

    def passenger_details(self):
        print("........Passenger Details........")
        print("Passenger ID:", self.passenger_id)
        print("Passenger Name:", self.name)
        print("Ticket Booked:", self.ticket)


obj = Bus()
while True:
    print("1.Add Passenger")
    print("2.Book Ticket")
    print("3.Cancel Ticket")
    print("4.Passenger Details")
    print("5.Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        obj.add_passenger()
    elif choice == 2:
        obj.book_ticket()
    elif choice == 3:
        obj.cancel_ticket()
    elif choice == 4:
        obj.passenger_details()
    elif choice == 5:
        print("Thank You....")
        print("Have a nice journey")
        break
    else:
        print("Invalid Choice")