def count(strn):
    vowels = []
    cons = []
    for i in strn:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            vowels.append(i)
        else:
            cons.append(i)
    if len(vowels) > 0:
        
        print(len(vowels),"vowels present")
        print("vowels are",str(vowels))
    else:
        print("no vowels found")
        
    print(len(cons),"consonents present")
    print("consonents are",str(cons))
    
strn = input("enter a string \n")

count(strn)