from abc import ABC,abstractmethod

class Bike(ABC):
    @abstractmethod
    def top(self):
        pass
    
    
class BMW(Bike):
    def top(self):
        print("top speed of 300kmph")
        
class Ducati(Bike):
    def top(self):
        print("top speed of 400kmph")
        
        
b1 = BMW()
b1.top()

b2 = Ducati()
b2.top()