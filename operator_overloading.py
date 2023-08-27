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
        
husband = Emp(10000,1000)
wife = Emp(9000,900)

combined = husband + wife 
print(combined.sal)

divided = husband - wife
print(divided.bon)