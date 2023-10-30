def count(strn):
    vowels = []
    cons = []
    #checking vowels or cons
    for i in strn:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            vowels.append(i)
        else:
            cons.append(i)
    #checking if there is vowels or not
    if len(vowels) > 0:
        
        print(len(vowels),"vowels present")
        print("vowels are",str(vowels))
    else:
        print("no vowels found")
    #checking if there is cons or not 
    if len(cons) > 0 :
           
        print(len(cons),"consonents present")
        print("consonents are",str(cons))
    else:
        print("no consonents found")
        
        
        
strn = input("enter a string \n").lower()

count(strn)