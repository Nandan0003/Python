#initializing pos to -1 as list starts from 0
pos = -1

# linaer search using while loop
def seach(listt,n):
    i = 0
    while i < len(listt):
        
        if listt[i] == n:
            globals()['pos'] = i  
            return True
        i += 1
    return False


# initializing list and assigning values
listt = [5,9,2,0,19,28]


n = 19


if seach(listt,n):
    print("found", pos)

else:
    print("not found")
    
   
#linear search using for loop   
    
def sear(listt,m):
    
    for j in range(0,len(listt)):
        if listt[j] == m:
            
            return j
            
    return -1
m = 0
        
res = sear(listt,m)

if(res == -1):
   print("not found") 
else:
    print("found at " + str(res))