class Student:
    def __init__(self):
        self.rollno = 0
        self.name = ""
        self.marks = 0

    def create_student(self):
        self.rollno = int(input("Enter the roll number: "))
        self.name = input("Enter the name: ")
        self.marks = int(input("Enter the marks: "))
        print("Student created successfully....!")

    def add_marks(self):
        mark = int(input("Enter the marks to add: "))
        self.marks += mark
        print("Marks added successfully....!")

    def update_marks(self):
        self.marks = int(input("Enter the new marks: "))
        print("Marks updated successfully....!")

    def display_marks(self):
        print("Marks:", self.marks)

    def student_details(self):
        print("........Student Details........")
        print("Roll Number:", self.rollno)
        print("Name:", self.name)
        print("Marks:", self.marks)


obj = Student()

while True:
    print("1.Create Student")
    print("2.Add Marks")
    print("3.Update Marks")
    print("4.Display Marks")
    print("5.Student Details")
    print("6.Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        obj.create_student()
    elif choice == 2:
        obj.add_marks()
    elif choice == 3:
        obj.update_marks()
    elif choice == 4:
        obj.display_marks()
    elif choice == 5:
        obj.student_details()
    elif choice == 6:
        print("Thank You....")
        break
    else:
        print("Invalid Choice")