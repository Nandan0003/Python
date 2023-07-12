print("welcome to the shop")

#asking name

name = input("enter ur name \n")

print("what would you like to have "+" " + name )

#Taking order
order = input("normal,black,strong,cold \n" )

if order == "normal":
    more = input("do u want sugar \n")
    if more == "yes":
        price = 25
    else:
        price = 20
           
elif order == "black":
    price = 12
elif order == "strong":
    price =13
elif order == "cold":
    price = 15
else :
    print("sorry we dont have that")
    exit()
#asking for quantity
quantity = int(input("how many coffee do u want \n"))

#calulating total price 
totalprice = quantity * price

print("ur total bills is  " + str(totalprice))



