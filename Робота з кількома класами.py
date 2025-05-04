class Student:
    def __init__(self, name):
        self.name = name
        self.knowledge = 0

    def learn(self):
        self.knowledge += 10
        print(f"{self.name} вивчає щось нове. Знання: {self.knowledge}")

class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self, student):
        print(f"{self.name} навчає {student.name}.")
        student.learn()

student = Student("Оля")
teacher = Teacher("Пані Марія")

for day in range(1, 6):
    print(f"\nДень {day}")
    teacher.teach(student)
