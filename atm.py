id = 3
name  = "nandan"
pws = 123
bal = 100

print("welcome to ATM")

cid = int(input("enter ur id"))
cpws = int(input("enter your password"))


if cid == id and cpws == pws:
    print("choose your option")
    ch = int(input(" 1.balance \n 2. withdraw \n 3.deposit \n 4.exit "))
    
    while ch > 0:
        if ch == 1:
            print(bal)
            break
        elif ch == 2:
            wtdrw = int(input("enter amout to withdraw"))
            if wtdrw > bal:
                print("balance is less than entered")
            else:
                bal -= wtdrw
                print("succesfully withdrawn and remaing balance is ",bal)
            break
        elif ch == 3:
            newamt = int(input("enter amount to deposit"))
            bal += newamt
            print("balance after deposit is",bal)
            break
        elif ch == 4:
            print("thank you")
            break
        else:
            print("enter valid choice")
            break
elif cid == id and cpws != pws:
    print("password not matching")
    
elif cid != id and cpws == pws:
    print("id  not matching")
    
else:
    print("id and password wont watch")