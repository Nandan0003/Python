#declraing funxtion 
def postfix(exp):
    #to store values calliong a list
    digitt = []
    #checking each and every element in expression
    for i in exp:
        #if the element iss digit then insert into lisit
        if i.isdigit():
            digitt.append(int(i))
        #else calculating exp
        else:
            #the first element coming out will be 2nd oprand as it is inserrted 2nd
            op2 = digitt.pop()
            #the seco9nd elemt coming out will be 1st operand as it is inserted 1st
            op1 = digitt.pop()
            
            #operators and their function
            if i == "+":
                res = op1 + op2
            elif i == "-":
                res = op1 - op2
            elif i == "*":
                res = op1 * op2
            elif i == "/":
                res = op1 / op2
            digitt.append(res)
    #return the elemnt of list at end of execution
    return digitt[0]

exp = "34+5-"
result = postfix(exp)
print(result)
