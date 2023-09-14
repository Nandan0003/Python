from  threading import Thread
from time import sleep



def Car():
    for i in range(5):
        print("my new car")
        sleep(2)
def Bike():
    for i in range(5):
        print("my new bike ")
        sleep(2)

class Super(Thread):
    def Bike(self):
        for i in range(5):
            print("my new bike ")
            sleep(2)
    

c =Thread( target=Car,args= ())       
c.start()


b =Thread( target=Bike,args= ())       
b.start()
c.join()
b.join()

s = Super()
s.start()
print("done")