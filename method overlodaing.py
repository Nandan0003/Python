
class new:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
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
print(a.mul(4,5))