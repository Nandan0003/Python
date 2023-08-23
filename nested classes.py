class Bike:
    def __init__(self,brand,ccubic,cylinder):
        self.brand = brand 
        self.ccubic = ccubic
        self.cylinder = cylinder
        self.new = self.Model("S1000RR")
        
    def show(self):
        print(f'{self.brand} has a {self.ccubic} capacity bike with {self.cylinder} cylinders')
        
        
    class Model:
        def __init__(self,bname):
            self.bname = bname
            
        def brand(self):
            print(f'A SUPER BIKE CALLED {self.bname}')
a = Bike("BMW",1000,4)
a.show()

x = a.new.brand()

#b = Bike.Model("S1000RR")
#b.brand()