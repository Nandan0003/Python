list1 = [5,2,4,1,6,4,8]

for i in range(0,len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i] >= list1[j]:
            list1[i],list1[j] = list1[j],list1[i]
            
print(list1)


list2 = [ 5,6,7,5,6,49,9]

lits2 = list2[ , ,-1]
print(list2)