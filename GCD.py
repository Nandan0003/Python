def gcd(a,b):
    while b != 0 :
        
        a,b = b,a%b
    return a    
a = int(input("enter a "))
b = int(input("enter b"))

sol = gcd(a,b)
print(sol)