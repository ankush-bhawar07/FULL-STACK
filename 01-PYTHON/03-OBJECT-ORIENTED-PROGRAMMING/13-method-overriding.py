class A:
    def show(self):
        print("In A show")

class B(A):
    def show(self):
        print("In B show")

a1 = A()
a1.show()

b1 = B()
b1.show()