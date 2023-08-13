
#function which checks if there is 10 or more characters
def l(ls):
    
    #input from user
    n = int(input("enter the size  \n"))
    
    for i in range(0,n):
        ele = input("enter element to list  \n ")
        
        ls.append(ele)
        
    #checking if there is more than 10    
    for j in ls:
        if len(j) > 10:
            
            ln.append(j)
        
            print("the name which has more thsn 10 characters is " + str(ln))   
        else:
            print("no name doesnt contain more than 10 characters")
ls = []
ln = []

#calling the function
l(ls)


