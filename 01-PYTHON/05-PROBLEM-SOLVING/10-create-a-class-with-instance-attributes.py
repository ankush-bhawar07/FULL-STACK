# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class Vecicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vecicle(170,20)
print(modelX.max_speed, modelX.mileage)