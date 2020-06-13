class student:
    school='success'
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    @classmethod
    def info(cls):
        return cls.school

s1=student(31,42,61)
s2=student(69,75,65)
print(student.info())
