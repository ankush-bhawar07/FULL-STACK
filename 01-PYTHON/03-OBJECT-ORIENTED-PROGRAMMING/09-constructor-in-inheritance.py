# constructor in inheritance
class A:
    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature 1-A is working")

    def feature2(self):
        print("Feature 2 is working")
        
class B():
    def __init__(self):
        print("in B init")
    def feature1(self):
        print("Feature 1-B is working")

    def feature4(self):
        print("Feature 4 is working")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("in C init")

    def feature5(self):
        print("feature 5 is working")

    def feature6(self):
        print("feature 6 is working")

a1 = A()
b1 = B()
c1 = C()

# method resolution order
c1.feature1()