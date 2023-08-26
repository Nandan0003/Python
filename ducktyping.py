class Bike:
    def start(self):
        print("Bike is ready to go")

class Car:
    def start(self):
        print("Car is ready to go")
        
        
class BMW:
    def new(self,bb):
        bb.start()
        
bb = Bike()

b = BMW()
b.new(bb)

cc = Car()

c = BMW()
c.new(cc)