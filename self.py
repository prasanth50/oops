class computer:
    def __init__(self):
        self.name='pro'
        self.age=22
    def update(self):
        self.age=25
        self.name='Reddy'
c1=computer()
c2=computer()
c1.update()
#c2.update()
print(c1.name)
print(c1.age)
print(c2.name)