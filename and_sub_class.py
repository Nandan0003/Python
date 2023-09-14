class sub:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def add(self):
        print(self.a + self.b)
    def mul(self):
        print(self.a * self.b)

class Main:
    
    a = sub(20,20)
    a.add()
    a.mul()

aa = Main()