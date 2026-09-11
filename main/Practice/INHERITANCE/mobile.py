class Mobile:
    def __init__(self):
        self.mobile_no = 0
        self.name = ""
        self.balance = 0

    def create_customer(self):
        self.mobile_no = int(input("Enter the mobile number: "))
        self.name = input("Enter the customer name: ")
        self.balance = float(input("Enter the balance: "))
        print("Customer created successfully....!")

    def recharge(self):
        amount = float(input("Enter the recharge amount: "))
        self.balance += amount
        print("Recharge successful....!")

    def check_balance(self):
        print("Balance:", self.balance)

    def customer_details(self):
        print("........Customer Details........")
        print("Mobile Number:", self.mobile_no)
        print("Customer Name:", self.name)
        print("Balance:", self.balance)


obj = Mobile()
while True:
    print("1.Create Customer")
    print("2.Recharge")
    print("3.Check Balance")
    print("4.Customer Details")
    print("5.Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        obj.create_customer()
    elif choice == 2:
        obj.recharge()
    elif choice == 3:
        obj.check_balance()
    elif choice == 4:
        obj.customer_details()
    elif choice == 5:
        print("Thank You and see you next time....")
        break
    else:
        print("Invalid Choice")