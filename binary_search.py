#initializing pos value to 0
pos = 0

#defining a function which returns true if find else return false
def b(ls,n):
    l = 0
    u = len(ls) - 1
    print(f'element to search is {n}')
    while l <= u:
    
        mid = (l+u) // 2
        
        if ls[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if ls[mid] < n:
                l = mid + 1 
            else:
                u = mid - 1
                
    return False    
 
#list 
ls  = [5,1,6,7,8,9,10]

#sorting a list
ls.sort()

#printing of sorted list
print(ls)

# value which we require
n = 10


#calling the function and checking if it is true or not
if b(ls,n) == True:
    print("found at",pos )
else:
    print("not found")        
