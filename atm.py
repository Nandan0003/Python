id = 3
name  = "nandan"
pws = 123
bal = 100

print("welcome to ATM \n")

cid = int(input("enter ur id \n"))
cpws = int(input("enter your password \n"))


if cid == id and cpws == pws:
    print("choose your option \n")
    ch = int(input(" 1.balance \n 2. withdraw \n 3.deposit \n 4.exit \n "))
    
    while ch > 0:
        if ch == 1:
            print(bal)
            break
        elif ch == 2:
            wtdrw = int(input("enter amout to withdraw \n"))
            if wtdrw > bal:
                print("balance is less than entered \n")
            else:
                bal -= wtdrw
                print("succesfully withdrawn and remaing balance is ",bal)
            break
        elif ch == 3:
            newamt = int(input("enter amount to deposit\n"))
            bal += newamt
            print("balance after deposit is",bal)
            break
        elif ch == 4:
            print("thank you ...")
            break
        else:
            print("enter valid choice ...!")
            break
elif cid == id and cpws != pws:
    print("password not matching ...!")
    
elif cid != id and cpws == pws:
    print("id  not matching ...!")
    
else:
    print("id and password wont watch ...!")