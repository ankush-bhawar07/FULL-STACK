class Computer:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def update(self):
        self.price = self.price + 5000
        print(self.price)

    def compare(self, other):
        if self.price == other.price:
            print("Same price")
        else:
            print("Difrent price")

comp1 = Computer("Lenovo", 47000)
comp2 = Computer("HP", 47000)

comp1.compare(comp2)
comp1.update()
comp1.compare(comp2)
