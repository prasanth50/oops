class student:
    school='success'
    def __init__(self):
        self.name='prasanth'
        self.age=22
        self.cls=10

    @staticmethod
    def info():
        print('This student is from this class')
s1=student()
s2=student()
student.info()
