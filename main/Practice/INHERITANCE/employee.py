class Employee:
    def __init__(self):
        self.emp_id = 0
        self.name = ""
        self.salary = 0

    def add_employee(self):
        self.emp_id = int(input("Enter the employee id: "))
        self.name = input("Enter the employee name: ")
        self.salary = float(input("Enter the salary: "))
        print("Employee added successfully....!")

    def update_salary(self):
        self.salary = float(input("Enter the new salary: "))
        print("Salary updated successfully....!")

    def display_salary(self):
        print("Salary:", self.salary)

    def employee_details(self):
        print("........Employee Details........")
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.name)
        print("Salary:", self.salary)


obj = Employee()
while True:
    print("1.Add Employee")
    print("2.Update Salary")
    print("3.Display Salary")
    print("4.Employee Details")
    print("5.Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        obj.add_employee()
    elif choice == 2:
        obj.update_salary()
    elif choice == 3:
        obj.display_salary()
    elif choice == 4:
        obj.employee_details()
    elif choice == 5:
        print("Thank you for your time....")
        break
    else:
        print("Invalid Choice")