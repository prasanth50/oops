class computer:
    def __init__(self):
        self.age=22
        self.name='pro'
    def update(self):
        self.age=25
    def compare(self,c2):
        if self.age==c2.age:
            return True
        else:
            return False
c1=computer()
c2=computer()
c1.update()
if c1.compare(c2):
    print('they are same')
else:
    print('they are different')

print(c1.name)
print(c1.age)
print(c2.name)
print(c2.age)
