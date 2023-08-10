#importing array module
import array as ar

#initiazing empty array
arr = ar.array('i',[])

#asking size of array from user
n = int(input("enter size of array \n"))

#getting elements from user
for i in range(n):
    ele = int(input("enter the values \n"))
    arr.append(ele)
    
#printing array    
print(arr)

#value to search
value = int(input("enter a value to search"))


#searching element
pos = 0

for j in arr:
    if j == value:
        print(f'found at {pos} \n')
    pos += 1
else:
    print("not found")








