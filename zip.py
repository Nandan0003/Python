#zip function is used to combine two or more list or tuple like structure to provide output as each element in preferred type



a = ["N","A","N","D","A","N"]

b = ["B","N","A","N","A","V"]

z = list(zip(a,b))
print(z)

for (a,b) in z:
    print(a,b)