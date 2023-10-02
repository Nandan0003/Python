def odd(n):
    tab = []
    for i in range(1,11):
        a = n * i 
        tab.append(a)
    print(tab)
def even(n):
    tab = []
    for i in range(1,11):
        a = n * i 
        tab.append(a)   
    print(tab)
n = int(input("enter a digit you need to get table of it \n"))

if n / 2 == 0:
    even(n)
else:
    odd(n)
    
    
    
