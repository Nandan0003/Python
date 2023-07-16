#names of all students attended online class
name = ['Abhi M','Bhavana C','Chethan T S','Akash S','Bhavana C','Chethan T S']

fake = []

for i in name:
    if i not in fake:
        fake.append(i)
        
#printing a list which has non repeated values
print(fake)
        

