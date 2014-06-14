def evalRPN(self, tokens):
    ops = ["+","-","*","/"]
    stack = []
    for i in range(len(tokens)):
        if tokens[i] not in ops:
            stack.append(int(tokens[i]))
        else:
            tmp1= stack.pop()
            tmp2= stack.pop()
            if tokens[i] in ops[0]:
                stack.append(tmp1+tmp2)
            elif tokens[i] in ops[1]:
                stack.append(tmp2-tmp1)
            elif tokens[i] in ops[2]:
                stack.append(tmp2*tmp1)
            elif tokens[i] in ops[3]:
                stack.append(int(float(tmp2)/float(tmp1)))
    return stack[-1]
                
