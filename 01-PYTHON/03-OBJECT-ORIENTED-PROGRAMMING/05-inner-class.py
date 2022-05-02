class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.id)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.ram = 4
        
        def show(self):
            print(self.brand, self.ram)

s1 = Student("John", 2)
s1.show()