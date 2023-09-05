def counting(str):
    count = 0
    space = 0
    for i in str:
        count += 1

        if i == " ":
            space += 1
            
        
    print("the no of characters in string is",count)
    print(f'the string has {space} no of spaces'}
    str = input("enter a string \n")

counting(str)
