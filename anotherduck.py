#class pen
class Pen:
    def write(self):
        print("pen will write")
#class pencil        
class Pencil:
    def write(self):
        print("pencil will write")
#class book       
class book:
    def write(self):
        print("bokk is both readble and writeable")
#class Any which is ducktyped can calledby any above classes the obejcts   
class Any:
    def any(self,objj):
        objj.write()
        
        
#object for pen       
ob1 = Pen()


#object for ducktyped class
ob2 = Any()
#calling function and passing pen object 
ob2.any(ob1)


ob3 = book()

ob4 = Any()
ob4.any(ob3)


#any class and objects can be passed to any so it calls directly