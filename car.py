car_state = ""
cond = False

while True:
    car_state = input(">").lower()
    if car_state == "start":
        if cond:
            print("car already started") 
        else:
            cond = True
            print("car started")
    
    
   
           
    elif car_state == "stop" :
        if cond == False:
            print("car already stopped")
        else:
            cond = False
            print("car stopped")
            
        
        cond = False
    
        
    elif car_state == "quit":
        break
    elif car_state == "help":
        print("start to start car \nstop to stop the car \n quit to quit the game")
    else:
        print("i dont understand")