car_state = ""
cond = False

while True:
#start the car
    car_state = input(">").lower()
    if car_state == "start":
        if cond:
            print("car already started") 
        else:
            cond = True
            print("car started")
    
    
  #stoping the car 
           
    elif car_state == "stop" :
        if cond == False:
            print("car already stopped")
        else:
            cond = False
            print("car stopped")
            
        
        
    
   #to quit the game     
    elif car_state == "quit":
        break
   #if user needs help
        
    elif car_state == "help":
        print("start to start car \nstop to stop the car \n quit to quit the game")
    #if the input is not understable to cpu
    else:
        print("i dont understand")

