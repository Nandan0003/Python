#initializing list
list1 = [5,2,4,1,6,4,8]

#checking cond if 1st ele to nth element and swap
for i in range(0,len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i] >= list1[j]:
            list1[i],list1[j] = list1[j],list1[i]

#print final list
            
print(list1)


