#zip function is used to combine two or more list or tuple like structure to provide output as each element in preferred type


#A list which has some characters
a = ["N","A","N","D","A","N"]
#B list which has some characters
b = ["B","N","A","N","A","V"]

z = list(zip(a,b))
print(z)

a = ["a","ab","t", "co", "i", "pyt"]
b = ["m","le","o","de","n","hon"]

coder = list(zip(a,b)) 

print("\n\n\n")

print("read by neglecting spaces")
for (a,b) in coder:
    print(a,b)