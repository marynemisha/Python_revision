class Bank:
    def __init__(self):
        self.account_number = 0
        self.name = ""
        self.balance = 0

    def create_account(self):
        self.account_number = int(input("Enter the account number: "))
        self.name = input("Enter the holder name: ")
        self.balance = float(input("Enter the balance: "))
        print("Account created successfully....!")

    def deposit(self):
        amount = float(input("Enter the deposit amount: "))
        self.balance += amount
        print("Deposit successful....!")

    def withdraw(self):
        amount = float(input("Enter the withdraw amount: "))
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful....!")
        else:
            print("Insufficient balance....!")

    def balance_enquiry(self):
        print("Balance:", self.balance)

    def account_details(self):
        print("........Account Details........")
        print("Account Number:", self.account_number)
        print("Holder Name:", self.name)
        print("Balance:", self.balance)


obj = Bank()
while True:
    print("1.Create Account")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Balance Enquiry")
    print("5.Account Details")
    print("6.Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        obj.create_account()
    elif choice == 2:
        obj.deposit()
    elif choice == 3:
        obj.withdraw()
    elif choice == 4:
        obj.balance_enquiry()
    elif choice == 5:
        obj.account_details()
    elif choice == 6:
        print("Thank you for your valuable time....")
        break
    else:
        print("Invalid Choice")