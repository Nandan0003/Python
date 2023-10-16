cond = False 

def light():
    clap = int(input("from censor returning 1 if clap is heard else 0 not heard \n"))
    if clap == 1:
        print("turning on lamp ")
        globals()['cond'] = True
        
    else:
        print("not heard and not turning lamp")
        globals()['cond'] =  False

light()