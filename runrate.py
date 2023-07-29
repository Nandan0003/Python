def runrate(runs_scored, balls_taken):
    try:
        return runs_scored/balls_taken*100 
        
    except ZeroDivisionError:
        print(" batsman cannot score on 0 balls and zero cannot be divided ")
      
runs_scored = int(input("enter how much batsman scored\n"))
balls_taken = int(input("enter the balls taken the batsman\n"))
    
print(runrate(runs_scored,balls_taken))
    