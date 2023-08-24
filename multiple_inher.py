class A:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("class a")   
        
    def add(self):
        print(int(self.a + self.b))
    
    
    
class B:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("b class")
    def sub(self):
        print(int(self.a - self.b))
    
class C(A,B):
    def __init__(self,a,b):
        self.a = a
        self.b = b
        super().__init__(1,2)
        print("c class")
    def mul(self):
        print(int(self.a * self.b))


a1 = A(4,5)
a1.add()

a2 = C(56,65)
a2.mul()
