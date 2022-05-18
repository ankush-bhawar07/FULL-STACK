# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
#  Given

class Vehicle:
    
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehicle):
    pass

b1 = Bus("School Volvo", 120, 12)
print(b1.name, b1.max_speed, b1.mileage)