class Electricity:
    def __init__(self):
        self.consumer_no = 0
        self.name = ""
        self.units = 0
        self.bill = 0

    def add_consumer(self):
        self.consumer_no = int(input("Enter the consumer number: "))
        self.name = input("Enter the consumer name: ")
        print("Consumer added successfully....!")

    def enter_units(self):
        self.units = int(input("Enter the units consumed: "))
        print("Units entered successfully....!")

    def calculate_bill(self):
        self.bill = self.units * 5
        print("Bill calculated successfully....!")

    def consumer_details(self):
        print("........Consumer Details........")
        print("Consumer Number:", self.consumer_no)
        print("Consumer Name:", self.name)
        print("Units:", self.units)
        print("Bill Amount:", self.bill)


obj = Electricity()
while True:
    print("1.Add Consumer")
    print("2.Enter Units")
    print("3.Calculate Bill")
    print("4.Consumer Details")
    print("5.Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        obj.add_consumer()
    elif choice == 2:
        obj.enter_units()
    elif choice == 3:
        obj.calculate_bill()
    elif choice == 4:
        obj.consumer_details()
    elif choice == 5:
        print("Thank You for choosing our service....")
        break
    else:
        print("Invalid Choice")