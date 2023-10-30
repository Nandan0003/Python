#importing threads and time module
from  threading import Thread
from time import sleep


#defining two functions 
def Car():
    for i in range(5):
        print("my new car")
        sleep(2)
def Bike():
    for i in range(5):
        print("my new bike ")
        sleep(2)


    
#initializing a threading variable and targetting a variable
c =Thread( target=Car,args= ())       
c.start()

#initializing a threading variable and targetting a variable
b =Thread( target=Bike,args= ())       
b.start()
#join fun is used to end main thread and then execute next
c.join()
b.join()

print("done")