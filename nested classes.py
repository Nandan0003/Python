class Bike:
    def __init__(self,brand,ccubic,cylinder):
        self.brand = brand 
        self.ccubic = ccubic
        self.cylinder = cylinder
        self.s = self.show()
    def show(self):
        print(f'{self.brand} has a {self.ccubic} capacity bike with {self.cylinder} cylinders')
        
        
    class Model:
        def __init__(self):
            self.bname = "BMW"
            
        def show(self):
            return self.bname
a = Bike("BMW",1000,4)
a.show()
a.Model.bname