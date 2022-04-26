class Greeting:
    def msg(self):
        print("Hello There")

greet = Greeting()
greet.msg()

class Computer:
    def confing(self):
        print("i5, 16gb, 1TB")

com1 = Computer()
Computer.confing(com1)

com2 = Computer()
Computer.confing(com2)

com1.confing()
com2.confing()
