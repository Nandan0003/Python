#creating a class 
class Cricketer:
    def __init__(self,name,role):
        self.name = name
        self.role = role
    
    def key(self):
        print(f"i am {self.name}and i play as {self.role }")
        
#creating an object of Cricketer class        
opt = Cricketer("nandan","all rounder")

#calling a class method
opt.key()