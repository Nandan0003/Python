def table():
    book = False
    
    while True:
        table1 = {
            "tableno1" : 1,
            "bookcond" : False,
            "name" : " "
        }
        table2 = {
            "tableno2" : 2,
            "bookcond" : True,
            "name" : " "
        }  
        
        table3 = {
            "tableno3" : 3,
            "bookcond" : False,
            "name" : ""
        }         
        
        tableno = int(input("enter a table no u want to book"))
        
        if tableno == 1 :
            if table1["bookcond"] == False:
                print("table is free and you can book \n")
                cond = input("Do u need to book if yes type : y if no : no \n").lower()
                if cond == "y":
                    name = input("enter your name \n")
                    table1["bookcond"] = True 
                    table1["name"] = name 
                    print("You booking is confirmed and details are \n")  
                    
                    print(str(table1)) 
                    exit()
                else:
                    print("thank you")
                    exit()
                
        elif tableno == 2 :
            if table2["bookcond"] == False:
                print("table is free and you can book")
                cond = input("Do u need to book if yes type : y if no : no \n").lower()
                if cond == "y":
                    name = input("enter your name \n")
                    table2["bookcond"] = True 
                    table2["name"] = name 
                    print("You booking is confirmed and details are \n")  
                    
                    print(str(table1)) 
                    exit()
                
                else:
                    print("thank you")
            
                    exit()
            elif table2["bookcond"] == True:
                print("The table is already booked, You can checkout any other table \n")
                      
        elif tableno == 3 :
            if table3["bookcond"] == False:
                print("table is free and you can book\n")
                cond = input("Do u need to book if yes type : y if no : \n").lower()
                if cond == "y":
                    name = input("enter your name\n")
                    table3["bookcond"] = True 
                    table3["name"] = name 
                    print("You booking is confirmed and details are \n")  
                    
                    print(str(table3)) 
                    exit()
                
                else:
                    print("thank you")
            
                    exit()
table()
        