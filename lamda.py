#to seperate odd and even in a list using lamda

nums = [5,9,75,4,2,1,3,5,4,4,65,54,44,476] 

odd = list(filter(lambda a:a%2 == 1,nums))

even = list(filter(lambda a:a%2 == 0,nums))


print(odd)

print(even)



cubes = list(map(lambda a: a*a*a,nums))
print(cubes)