class top:
    def __init__(self):
        self.num = 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num <= 10:
            sqr = self.num * self.num
            self.num +=1
            
            return sqr
        
        else:
            raise StopIteration
        
        
new = top()
for i in new:
    print(i)