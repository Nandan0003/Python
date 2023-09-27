def postfix(exp):
    digitt = []
    for i in exp:
        if i.isdigit():
            digitt.append(int(i))
        else:
            op2 = digitt.pop()
            op1 = digitt.pop()
            if i == "+":
                res = op1 + op2
            elif i == "-":
                res = op1 - op2
            elif i == "*":
                res = op1 * op2
            elif i == "/":
                res = op1 / op2
            digitt.append(res)
    return digitt[0]

exp = "34+5-"
result = postfix(exp)
print(result)
