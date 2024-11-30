import csv
from lab10 import Manager
from lab10 import Worker

class FileHandler:
    @staticmethod
    def save_employees(employees, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for employee in employees:
                if isinstance(employee, Manager):
                    writer.writerow([
                        employee.get_name(), employee.get_age(),
                        employee.get_salary(), employee.get_department(), ''
                    ])
                elif isinstasnce(employee, Worker):
                    writer.writerow([
                        employee.get_name(), employee.get_age(),
                        employee.get_salary(), '', employee.get_hours_worked()
                    ])

    @staticmethod
    def load_employees(filename):
        employees = []
        try:
            with open(filename, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    name, age, salary, department, hours_worked = row
                    if department:
                        employees.append(Manager(name, int(age), int(salary), department))
                    elif hours_worked:
                        employees.append(Worker(name, int(age), int(salary), int(hours_worked)))
        except FileNotFoundError:
            pass
        return employees

def main():
    filename = "employees.csv"
    employees = FileHandler.load_employees(filename)

    while True:
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Save and Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_employee(employees)
        elif choice == 2:
            display_employees(employees)
        elif choice == 3:
            update_employee(employees)
        elif choice == 4:
            delete_employee(employees)
        elif choice == 5:
            FileHandler.save_employees(employees, filename)
            break

if _name_ == "_main_":
    main()