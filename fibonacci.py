#initialing the values for a,b,last
a = 0
b = 1
last = 0

#declaring a new empty list to store the fibonacci series

latest = []

#taking user input till n will be initiated
n = int(input("enter n \n"))

#first append the last then 
latest.append(last)

#checking the conditions for fibonacci
while n > last:
        
    a = b
    b = last
    last = a + b
    latest.append(last)
    
#at last print lat3est list of fibonacci series
print(latest)
    
