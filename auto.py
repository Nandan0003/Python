cond = False 

def light():
    clapcount = int(input("from censor returning count of claps \n"))
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