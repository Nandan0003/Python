#class 
class movies:
    
    #class variable
    industry = "SANDALWOOD"
    
    
    def __init__(self,hero,heroine,year,movie):
        self.hero = hero
        self.heroine = heroine
        self.year = year
        self.movie = movie
        
    #instance method   
    def title(self):
        print(f'{self.hero} is with {self.heroine} and in year {self.year} for a big movie called  {self.movie} ')
        
    #class method
    #@classmethod
    def indus(cls):
        print(cls.industry)  

    #static method
    @staticmethod
    def info():
        print("\nall are HIT movies in KANNADA andEVERYWHERE\n")
        
  
    
#calling all function
       
movies.indus()       
y = movies("yash","srinidhi",2019,"kgf")
y.title()

movies.indus()  
s = movies("sudeep","neetha ashok",2022,"vikrath rona")
s.title()

movies.indus.cls()  
sh = movies("shivanna","adithi",2023,"vedha")
sh.title()

movies.info()