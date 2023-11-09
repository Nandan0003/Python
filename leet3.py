class sol:
    def __init__(self,l1,l2):
        self.l1 = l1
        self.l2 = l2 
        
        
    def li(self):
        ll1 = " "
        for i in l1:
            ll1 += str(i)
            
        ll2 = " "
        for i in l2:
            ll2 += str(i)
            
            
            
        sum = int(ll1) + int(ll2)
        
        sum = str(sum)
        print(sum[::-1])
        
        
l1 = [2,4,3]
l2 = [5,6,4]

a = sol(l1,l2)
a.li()