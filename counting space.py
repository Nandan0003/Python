def spaces(str):
    count = 0
    for i in str:
        if i == " ":
            count += 1
    print(count)     
str = input("enter a string ")
spaces(str)



a  = "nanfdan"
n = a[0]

for i in a:
    if i == n:
        print("repeats",i)

def lenth(str):
    count = 0
    for i in str:
        count += 1
    print(count)

str = input("enter a string")
lenth(str)