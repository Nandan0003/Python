#priortize condition false coz at start no ntg is heard
cond = False 

def light():
    #here am taking count from user but we can automate through censors
    clapcount = int(input("from censor returning count of claps \n"))
    
    #different types of scenario for different count 
    if clapcount == 0:
        print("not heard and not turning on anything")
        globals()['cond'] =  False

    elif clapcount == 1:
        print("turning on lamp ")
        globals()['cond'] = True
    
    elif clapcount  == 2:
        print("turning on fan")  
        globals()['cond'] = True
    elif clapcount  == 3:
        print("turning on AC")  
        globals()['cond'] = True
    else:
        print("Value not assingned and no action found")
        globals()['cond'] =  False
            
    
light()