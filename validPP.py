def vp(s):
    stack = []
    cnt = i = best = 0
    while i < len(s):
        if len(stack)==0 and i !=0:
            cnt = 0
        if s[i]=='(':
            stack.append(i)
        elif s[i]==')' and len(stack)>0:
            stack.pop()
            cnt+=2
            best = max(best,cnt)
        i+=1
    return cnt
        
s=')()())'
s='(((()))'
