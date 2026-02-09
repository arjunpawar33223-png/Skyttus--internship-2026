class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_salary(self):
        print(f"{self.name}'s salary: {self.salary}")

# Example
emp = Employee("Arjun", 50000)
emp.display_salary()