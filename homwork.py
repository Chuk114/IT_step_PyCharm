class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_salary_info(self):
        return f"Заробітна плата {self.name}: {self.salary}"


emp = Employee("Олексій", "Інженер", 20000)

print(emp.get_salary_info())
