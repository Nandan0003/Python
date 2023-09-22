
### NOTE: I will be trying method this is sample and for my learninng ###


#string input
str  = input("enter a string\n")

#input and searc of replacement word

word = input("enter a word which should be replaced\n")


#word for replacement
replace = input(f"enter a word what should be replaced in place of {word} \n")

#empty string
s = ""

#for space
space = " "

#splitting the ip string
new  = str.split(" ") 


#checking condition matching with replacemnt word and replaing with new word
for i in new:
    if i == word:
        s += replace
        s += space
        
        
        
    else:
        s += i 
        s += space
        
#printing new string
print(s)        


