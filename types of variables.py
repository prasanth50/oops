class car:
    wheels=4
    def __init__(self):
        self.mil=10
        self.name="BMW"
c1=car()
c2=car()

c1.mil=20
car.wheels=5

print(c1.name,c1.mil,c1.wheels)
print(c2.name,c2.mil,c2.wheels)