class Human:
    def __init__(self, name="Name"):
        self.name = name

class Car:
    def __init__(self, brand="Porsche"):
        self.brand = brand
        self.passengers = []

    def add_passengers(self, *args):
        self.passengers.extend(args)

    def print_passengers(self):
        if self.passengers:
            names = ", ".join(i.name for i in self.passengers)
            print(f"Names of {self.brand} passengers: {names}")
        else:
            print(f"In the car {self.brand} there are no passengers.")

dima = Human("Dmytro")
ihor = Human("Ihor")

car1 = Car("Mercedes")
car2 = Car()

car2.print_passengers()
car1.add_passengers(ihor, dima)
car1.print_passengers()
