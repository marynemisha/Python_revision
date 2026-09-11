class Hospital:
    def __init__(self):
        self.patient_id = 0
        self.name = ""
        self.disease = ""

    def add_patient(self):
        self.patient_id = int(input("Enter the patient id: "))
        self.name = input("Enter the patient name: ")
        self.disease = input("Enter the disease: ")
        print("Patient added successfully....!")

    def book_appointment(self):
        print("Appointment booked successfully....!")

    def update_patient_details(self):
        self.name = input("Enter the new patient name: ")
        self.disease = input("Enter the new disease: ")
        print("Patient details updated successfully....!")

    def patient_details(self):
        print("........Patient Details........")
        print("Patient ID:", self.patient_id)
        print("Patient Name:", self.name)
        print("Disease:", self.disease)


obj = Hospital()
while True:
    print("1.Add Patient")
    print("2.Book Appointment")
    print("3.Update Patient Details")
    print("4.Patient Details")
    print("5.Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        obj.add_patient()
    elif choice == 2:
        obj.book_appointment()
    elif choice == 3:
        obj.update_patient_details()
    elif choice == 4:
        obj.patient_details()
    elif choice == 5:
        print("Thank you for your valuable time...")
        print("see you next time")
        break
    else:
        print("Invalid Choice")