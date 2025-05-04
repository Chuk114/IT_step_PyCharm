import random


class Student:
    def __init__(self, name):
        self.name = name
        self.knowledge = 0

    def learn_from_teacher(self, teacher):
        teacher.teach(self)

    def learn_from_library(self, library):
        library.provide_knowledge(self)

    def __str__(self):
        return f"{self.name} | Знання: {self.knowledge}"


class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self, student):
        print(f"{self.name} навчає {student.name}.")
        student.knowledge += 10


class Library:
    def __init__(self):
        self.knowledge_available = 5

    def provide_knowledge(self, student):
        print(f"{student.name} читає в бібліотеці.")
        student.knowledge += self.knowledge_available



student = Student("Оля")
teacher = Teacher("Пані Марія")
library = Library()


for day in range(1, 6):
    print(f"\n📅 День {day}")
    action = random.choice(["teacher", "library"])

    if action == "teacher":
        student.learn_from_teacher(teacher)
    else:
        student.learn_from_library(library)

    print(student)
