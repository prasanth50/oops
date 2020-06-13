class student:
    def __init__(self,name,roolno):
        self.name=name
        self.roolno=roolno
        self.lap=self.laptop()
    def show(self):
        print(self.name,self.roolno)
        self.lap.show()
    class laptop:
        def __init__(self):
            self.brand='HP'
            self.cpu='i5'
            self.ram=8
        def show(self):
            print(self.brand,self.cpu,self.ram)
s1=student('pro',2)
s2=student('ram',10)
s1.show()
s2.show()

