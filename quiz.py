name = input("Enter your name \n").capitalize()

print(f"hii {name} welcome to the quiz \n")

while True:
    count = 0 
    print("who is author of python\nselect options only \na.guido van russom \nb.james goslings \nc.bjarne strostoup \n")

    a = input("enter your answer").lower()
    if a == "a":
        print("yes,continue")
        count += 1
    else:
        print("you failed ")
        break
        exit()
    
    print("python was introduced in \nselect options only \na.2000 \nb.1999 \nc.1991 \n")

    a = input("enter your answer").lower()
    if a == "c":
        print("yes,continue")
        count += 1
    else:
        print("you failed ")
        break
        exit()
    print("is python interpreted or compiled \nselect options only \na.interpreted \nb.compiled \nc.both \n")

    a = input("enter your answer").lower()
    if a == "a":
        print("yes,continue")
        count += 1
    else:
        print("you failed ")
    break
        
if count > 2:
      

    print(f"Thank you {name}for taking quiz you scored out of 3 is ",str(count),"That is excellent")
    
elif count > 1:
    print(f"Thank you {name}for taking quiz you scored out of 3 is ",str(count),"That is quite good but nned to work")
    
else:
    print("poor and need to work very hard")