import random

class Student:
    def __init__(self, name):
        self.name = name
        self.knowledge = 50
        self.energy = 50
        self.mood = 50
        self.money = 100

    def study(self):
        print(" Навчається")
        self.knowledge += 5
        self.energy -= 10
        self.mood -= 5

    def work(self):
        print(" Працює")
        self.money += 50
        self.energy -= 15
        self.mood -= 10

    def rest(self):
        print(" Відпочиває")
        self.energy += 20
        self.mood += 10
        self.money -= 10

    def daily_needs(self):

        if self.money < 20:
            self.work()
        elif self.knowledge < 40:
            self.study()
        elif self.energy < 30:
            self.rest()
        else:
            choice = random.choice(['study', 'rest', 'work'])
            if choice == 'study':
                self.study()
            elif choice == 'rest':
                self.rest()
            else:
                self.work()

    def show_status(self, day):
        print(f"\n День {day}")
        print(f"Ім'я: {self.name}")
        print(f"Знання: {self.knowledge}")
        print(f"Енергія: {self.energy}")
        print(f"Настрій: {self.mood}")
        print(f"Гроші: {self.money}")

    def live_year(self):
        for day in range(1, 366):
            self.daily_needs()
            self.show_status(day)


student = Student("Андрій")

student.live_year()
