#a class 
class new:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

#    
        
    def add(self):
        sum = 0 
        
        sum = self.a + self.b + self.c
        print(sum)
    
    def mul(self,m = None,n = None, o = None):
        prod = 0
        if m != None and n != None and o != None:
            prod = m * n * o
            
        elif m != None and n != None:
            prod = m * n
            
        else:
            prod = m
        return prod
a = new(4,5,6)
a.add()
print(a.mul(4,5))