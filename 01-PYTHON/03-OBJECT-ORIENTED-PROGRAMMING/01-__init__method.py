class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def data(self):
        print(self.name, self.id)

s1 = Student("Ankush", 1)
s1.data()
