#creating a base class
class Inher:
    def __init__(self,name):
        self.name = name
        
        
    def nan(self):
        print(f"i am {self.name}")
        
        
 #creating a inherteing class 1 of base class       
class Batsman(Inher):
    pass

#creating a inherteing class 2 of base class  
class Bowler(Inher):
    pass

#inittializing and calling base class 
a = Inher("Nandan")
a.nan()


#inittializing and calling inhereted  class which makes same operation as base 
b = Batsman("Kumar")  
b.nan()


#inittializing and calling inhereted  class which makes same operation as base 
c = Bowler("M")
c.nan()