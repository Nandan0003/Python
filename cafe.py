


#Semi done 

print("greetings to everyone \n")

total = 0

def menu():
    dish = []


    typee = input("what type would you like to have \n 1.South Indian \n 2.North Indian \n 3.Chinese \n ").lower()

    if typee == "south indian" or typee == "1":
        
        n = int(input("enter how many south indian dishes u need"))
        for i in range(n):
            
            order = input(" Select your Meals \n 1.South Full Meals \n 2.Plate Meals \n 3.MasalDosa \n 4.Pongal ").lower()
            dish.append(order)
            if order == "southfull meals" or order == "1":
                fp = 100
            elif order =="plate meals" or order == "2":
                hp = 70
            elif order =="masal dosa" or order == "3":
                mp = 60
            elif order == "pongal" or order == "4":
                pp = 70
            else:
                print("dish not available")
      
        for i in dish:
            if i == "full meals" or i == "1":
                globals()['total'] += fp
            elif i == "plate meals" or i == "2":
                globals()['total'] += hp 
            elif i == "masal dosa" or i == "3":
                globals()['total'] += mp 
            else:
                globals()['total'] += pp
    elif typee == "north indian" or typee == "2":
        
        n = int(input("enter how many north indian dishes u need"))
        for i in range(n):
            
            order = input(" Select your Meals \n 1.North Full Meals \n 2.Chole Bature \n 3.Roti kulcha \n 4.Dhal kichdi ").lower()
            dish.append(order)
            if order == "north full meals" or order == "1":
                fp = 200
            elif order =="chole bature" or order == "2":
                hp = 150
            elif order =="roti kulcha" or order == "3":
                mp = 120
            elif order == "dhal kichdi" or order == "4":
                pp = 50
        
     
        for i in dish:
            if i == "full meals" or i == "1":
                globals()['total'] += fp
            elif i == "plate meals" or i == "2":
                globals()['total']+= hp
            elif i == "masal dosa" or i == "3":
                globals()['total'] += mp 
            else:
                globals()['total'] += pp
    
    print(dish)       
    

menu() 


new = input("do u need to order again \n yes or no \n")

if new  == "yes":
    menu()

    
print(f"thank you for visiting and the total bill is {total}")

