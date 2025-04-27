class Human:
    def __init__(self, name="Name"):
        self.name = name

class Car:
    def __init__(self, brand="Porsche"):
        self.brand = brand
        self.passengers = []

    def add_passengers(self, human):
        self.passengers.append(human)
    def print_passengers(self):
        if self.passengers:  # Без крапок після if
            print(f"Names of {self.brand} passengers:")
            for i in self.passengers:
                print(i.name)
        else:
            print(f"{self.brand} has no passengers.")


dima = Human("Dmytro")
ihor = Human("Ihor")
car1 = Car("Mercedes")
car2 = Car()
car2.add_passengers(dima)
car1.add_passengers(ihor)
car1.print_passengers()
car2.print_passengers()
