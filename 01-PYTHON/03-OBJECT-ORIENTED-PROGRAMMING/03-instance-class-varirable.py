class Car:
    type = "SUV"
    def __init__(self):
        self.brand = "Mercedes"
        self.milage = 7

car1 = Car()
car2 = Car()

car1.brand = "Tata"
Car.type = "Compact-SUV"
print(car1.brand, car1.milage, car1.type)
print(car2.brand, car2.milage, car2.type)
