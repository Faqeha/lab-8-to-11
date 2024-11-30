class Employee:
    def _init_(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def display_info(self):
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")
        print(f"Salary: {self.__salary}")

class Manager(Employee):
    def _init_(self, name, age, salary, department):
        super()._init_(name, age, salary)
        self.__department = department

    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.__department}")

class Worker(Employee):
    def _init_(self, name, age, salary, hours_worked):
        super()._init_(name, age, salary)
        self.__hours_worked = hours_worked

    def get_hours_worked(self):
        return self.__hours_worked

    def set_hours_worked(self, hours_worked):
        self.__hours_worked = hours_worked

    def display_info(self):
        super().display_info()
        print(f"Hours Worked: {self.__hours_worked}")