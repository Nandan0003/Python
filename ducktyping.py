#class of bike
class Bike:
    def start(self):
        print("Bike is ready to go")
#class of car
class Car:
    def start(self):
        print("Car is ready to go")
        
#class of BMW which has method calling start method for instance variable so it calls start method of both class        
class BMW:
    def new(self,bb):
        bb.start()
        
bb = Bike()

b = BMW()
b.new(bb)

cc = Car()

c = BMW()
c.new(cc)


dd = Car()
d = BMW()
d.new(dd)


class sub:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def add(self):
        print(self.a + self.b)
    def mul(self):
        print(self.a * self.b)

class Main:
    
    a = sub(20,0)
    a.add()
    a.mul()

aa = Main()