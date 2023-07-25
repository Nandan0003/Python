#importing random module 
import random


#class which has both six and four digit otp methods
class Otp:
    def sixdigit(self):
        six = (random.randint(1,9),random.randint(1,9),random.randint(1,9),random.randint(1,9),random.randint(1,9),random.randint(1,9))
        
        return six
    
    def fourdigit(self):
        
        four = (random.randint(1,9),random.randint(1,9),random.randint(1,9),random.randint(1,9))
        
        return four
    
#initializing a object for class 
otp = Otp()

#first calling a six digit otp function or four digit can also called

#in two methods any of one method can be called based on requirements
s = otp.sixdigit()


f = otp.fourdigit()

#printing random otp
print(s)

print(f)