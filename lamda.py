#to seperate odd and even in a list using lamda


#defining a list
nums = [5,9,75,4,2,1,3,5,4,4,65,54,44,476] 

#a lamda function which returns list with odd only

odd = list(filter(lambda a:a%2 == 1,nums))


#a lamda function which returns list with even only

even = tuple(filter(lambda a:a%2 == 0,nums))


print(odd)

print(even)


#printing a cube of all nos in a list using map function

cubes = list(map(lambda a: a*a*a,nums))
print(cubes)