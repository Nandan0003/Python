id = 3 



Python = {
    "bookid" : 1,
    "quantity" : 5
}
    
Java = {
    "bookid" : 2,
    "quantity" : 2
}


C = {
    "bookid" : 3,
    "quantity" :4
}

def library():
    count = 0
    
    while True:
        Stud = int(input("enter your id \n"))
        
        if Stud == 3:

            book = input("enter which book do u want \n").lower()
            
            if book == "python" and Python["quantity"] > 1:
                count += 1
                Python["quantity"] -= 1
                print(f"issued and book need to return is {count}")
            elif book == "java" and Java["quantity"] > 1:
                count += 1
                Java["quantity"] -= 1
            elif book == "c" and C["quantity"] > 1:
                count += 1
                C["quantity"] -= 1
            else:
                print("not available right now")   
        again = input("do u need to purchase again \n \n")
        if again == "yes":
            pass
        else:
            print(Python["quantity"])
            print(Java["quantity"])
            print(C["quantity"])
            exit()

       
library()