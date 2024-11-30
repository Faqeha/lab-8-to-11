class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name: ", self.name)
        print("Age: ", self.age)

class Employee:
    def __init__(self, employee_id, position):
        self.employee_id = employee_id
        self.position = position

    def display_info(self):
        print("Empolyee ID: ", self.employee_id)
        print("Employee Position: ", self.position)

class Staff(Person, Employee):
    def __init__(self, name, age, employee_id, position, department):
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, position)
        self.department = department

    def additional_info(self):
        print("Department: ", self.department)

def read_employees_from_file(file_name):
    employees = []

    try:
        with open(file_name, 'r') as file:
            for line in file:
                data = line.strip().split(",")
                name, age, employee_id, position, department = data
                employees.append(Staff(name, int(age), employee_id, position, department))
    except FileNotFoundError:
        print(f"{file_name} not found. Starting with no employees.")
    return employees

def write_employees_to_file(file_name, employees):
    with open(file_name, 'w') as file:
        for emp in employees:
            file.write(f"{emp.name},{emp.age},{emp.employee_id},{emp.position},{emp.department}\n")

def add_employee(employees):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    employee_id = input("Enter employee ID: ")
    position = input("Enter position: ")
    department = input("Enter department: ")
    employees.append(Staff(name, age, employee_id, position, department))


file_name = "employees.txt"
employees = read_employees_from_file(file_name)

while True:
    print("\nMenu:")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Save and Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee(employees)
    elif choice == "2":
        for emp in employees:
            emp.display_info()
            emp.additional_info()
            print()
    elif choice == "3":
        write_employees_to_file(file_name, employees)
        print("Data saved. Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
