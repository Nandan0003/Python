#initialing the values for a,b,last
a = 0
b = 1
last = 0

#declaring a new empty list to store the fibonacci series

latest = []

#taking user input till n will be initiated
n = int(input("enter n \n"))
#to take count because the series must be continued till n
count = 0


#checking the conditions for fibonacci
while count < n:
    latest.append(last) 
    last = a + b
    a = b
    b = last
    
    count += 1
    
#at last print lat3est list of fibonacci series
print(latest)
    
