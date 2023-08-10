import array as ar

arr = ar.array('i',[])

n = int(input("enter size of array \n"))

for i in range(n):
    ele = int(input("enter the values \n"))
    arr.append(ele)
    
print(arr)

value = int(input("enter a value to search"))

pos = 0

for j in arr:
    if j == value:
        print(f'found at {pos} \n')
    pos += 1