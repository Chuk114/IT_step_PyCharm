class Student:
 amount_of_students = 0
 def __init__(self, height=160):
 self.height = height
 Student.amount_of_students+=1
 def grow(self, height=1):
 self.height+=height
mark = Student()
artem = Student(height=170)
mark.grow(height=15)
print(artem.height)
print(mark.height)