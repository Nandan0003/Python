def sortt(lisss):
    #n is length of listt passed
    
    n = len(lisss)
    
    #for loop from 0 to end of list
    for i in range(0,n):
        
        
        #assuming first elent is minimum
        min = i 
        
        
        #nested loop for checking condition min is less than next elements
        for j in range(i,n):
            
            
            #checking j value is less than value
            if lisss[j] < lisss[min]:
                
                
                #if j < min then reinitialize j as min
                min = j
                
                
        #swap i and min       
        lisss[i],lisss[min] = lisss[min],lisss[i]
        
        
    print(lisss)   


lisss = [5,6,7,2,6,9,5]
sortt(lisss)
