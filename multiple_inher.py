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
        super().__init__(a,b)
        print("c class")
    def mul(self):
        print(int(self.a * self.b))
        
        
class D(C):
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("class d")

    def div(self):
        try:
            dd = (self.a / self.b)
            print(dd)
        except ZeroDivisionError:
            print(f'{self.b} cant be zero')


a1 = A(4,5)
a1.add()

a2 = C(56,65)
a2.mul()

a3 = D(4,5)
a3.sub()

a4 = B(4,6)
a4.sub()