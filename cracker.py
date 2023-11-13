def sky():
    print("firing skyshot ")
    
def atom():
    print("firing atom bomb")

def krish():
    print("spinning and firing the chakra")
    
choice = int(input("enter your choice \n 1.Skyshot \n 2.AtomBomb \n 3.Krish \n 4.do u need to burn all \n"))

if choice == 1:
    sky()
elif choice == 2:
    atom()
elif choice == 3:
    krish()
elif choice == 4:
    sky()
    atom()
    krish()
else:
    print("select the desired choice")   
print("Burn low crackers and dont burn if possible")


