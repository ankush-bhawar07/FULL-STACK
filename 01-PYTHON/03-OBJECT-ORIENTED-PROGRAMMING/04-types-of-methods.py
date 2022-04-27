class Student:
    school = "CodeCompete"
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def information():
        return "this is CodeCompete"

s1 = Student(85,86,87)
s2 = Student(99,87,88)

print(s1.avg())
print(s2.avg())
print(Student.getSchool())
print(Student.information())


