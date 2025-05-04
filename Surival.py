import random

brands_of_car = ["BMW", "Lada", "Volvo", "Kia"]
job_list = [
    {"job": "Java developer", "salary": 50, "gladness_less": 10},
    {"job": "Python developer", "salary": 40, "gladness_less": 3},
    {"job": "C++ developer", "salary": 45, "gladness_less": 25},
]

class House:
    def __init__(self):
        self.food = 50
        self.mess = 0

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.fuel = 100
        self.strength = 100
        self.consumption = 10

    def drive(self):
        if self.fuel >= self.consumption and self.strength > 0:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            return False

class Job:
    def __init__(self, job_info):
        self.job = job_info["job"]
        self.salary = job_info["salary"]
        self.gladness_less = job_info["gladness_less"]

class Human:
    def __init__(self, name="Name", job=None, home=None, car=None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.gladness = 50
        self.satiety = 50

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(random.choice(brands_of_car))

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(random.choice(job_list))

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                return
            else:
                self.satiety += 5
                self.home.food -= 5

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < self.car.consumption:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel <= self.car.consumption:
                manage = "fuel"
            else:
                self.to_repair()
                return

        if manage == "fuel":
            self.car.fuel += 100
            self.money -= 100
        elif manage == "food":
            self.home.food += 50
            self.money -= 50

    def days_indexes(self, day):
        title = f"Today the {day} of {self.name}'s life"
        print(f"{title:^50}", "\n")

        print(f"{self.name}'s indexes".center(50), "\n")
        print(f"Money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")

        print("Home indexes".center(50), "\n")
        print(f"Food - {self.home.food}")
        print(f"Mess - {self.home.mess}")

        print(f"{self.car.brand} car indexes".center(50), "\n")
        print(f"Fuel - {self.car.fuel}")
        print(f"Strength - {self.car.strength}")

    def is_alive(self):
        if self.satiety < 0:
            print("Dead...")
            return False
        if self.money < -500:
            print("Bankrupt...")
            return False
        if self.gladness < 0:
            print("Depression...")
            return False
        return True

    def live(self, day):
        if not self.is_alive():
            return False

        if self.home is None:
            self.get_home()
            print("Settled in the house!")

        if self.car is None:
            self.get_car()
            print(f"I bought car {self.car.brand}!")

        if self.job is None:
            self.get_job()
            print(f"Going to get a job {self.job.job}, with salary {self.job.salary}!")

        self.days_indexes(day)

        if self.satiety < 20:
            print("I am going to eat.")
            self.eat()

        elif self.gladness < 20:
            if self.home.mess > 20:
                print("I will clean my home.")
                self.clean_home()
            else:
                print("Let's chill!")
                self.chill()

        elif self.money < -50:
            print("Start working.")
            self.work()





