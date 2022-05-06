a = 5
b = 7

print(a + b)
print(int.__add__(a,b))

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3

    def __str__(self):
        # return self.m1, self.m2
        return '{} {}'.format(self.m1, self.m2)


s1 = Student(87,97)
s2 = Student(89,98)

s3 = s1 + s2
print(s3.m1)
print(s3.m2)
print(s1.__str__())
