#problem to combine to or more list which does not accepts 0
num1 = [1,2,3,4]
num2 = [5,6,7]
num3 = []

n = len(num1)
i = 0
while i < n:
    if num1[i] != 0:
        num3.append(num1[i])
    i += 1
        
n = len(num2)
i = 0
while i < n:
    if num2[i] != 0:
        num3.append(num2[i])
    i += 1


print(num3)


    