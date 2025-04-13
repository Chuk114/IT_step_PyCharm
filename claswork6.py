class Student:
    number = 0

    def __init__(self, height = 164, name = None):
        self.height = height
        self.name = name
        Student.number = Student.number + 1

    def grow(self, height = 3):
        self.height = self.height + height

    def __str__(self):
        return f"Я студент, з іменем {self.name} Мій зріст = {self.height}"

Artem = Student(height = 170, name="Artem")
Mark = Student(name="Mark")

print(Artem)
print(Mark)

while Mark.height < 180:
    Mark.grow()
    print("My height = ", Artem.height)
    print("My height = ", Mark.height)

print("number of students = ", Student.number)


