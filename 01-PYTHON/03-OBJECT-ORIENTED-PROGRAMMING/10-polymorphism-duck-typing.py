# duck typing
class Pycharm:
    def execute(self):
        print("Comipling")
        print("Running")

class MyEditor:
    def execute(self):
        print("Spell check")
        print("Convention check")
        print("Comipling")
        print("Running")

class Laptop:
    def code(self, ide):
        ide.execute()

ide1 = Pycharm()
ide2 = MyEditor()
lap1 = Laptop()

lap1.code(ide1)