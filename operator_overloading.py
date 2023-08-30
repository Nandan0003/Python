class Emp:
    def __init__(self,sal,bon):
        self.sal = sal
        self.bon = bon
        
        
        
        
    def __add__(self,other):
        sal = self.sal + other.sal 
        bon = self.bon + other.bon 
        combined = Emp(sal,bon)
        return combined

    def __sub__(self,other):
        sal = self.sal - other.sal 
        bon = self.bon - other.bon 
        divided  = Emp(sal,bon)
        return divided
     
    def __mul__(self, other):
        sal = self.sal * other.sal 
        bon = self.bon * other.bon 
        mull = Emp(sal,bon)
        return mull
    
    def __gt__(self,other):
        if self.sal > other.sal:
            print(f'{self.sal} is more')
        else:
            print(f'{other.sal} is more')
            
    def __lt__(self,other):
        if self.bon < other.bon:
            return True
        else:
            return False 
#new objects ffor class
husband = Emp(10000,1000)
wife = Emp(9000,900)

combined = husband + wife 
print(combined.sal)

divided = husband - wife
print(divided.bon)

mull = husband * wife
print(mull.bon)

gt = husband > wife

lt = husband < wife
if lt:
    print("husband has less")
else:
    print("wife has less")

