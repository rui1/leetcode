def partitionw(s):
    if s:
        pre = [[s[0]]]
        #print(pre)
        for i in range(1,len(s)):
            tmp = []
            #print(i,s[i],pre,tmp)
            for x in pre:
                #print("x",x,"s[i]",s[i])
                tmp.append(x+[s[i]])
                #print("first tmp",tmp)
                if x[-1]+s[i]==(x[-1]+s[i])[::-1]:
                    tmp1 = x[:-1]+[x[-1]+s[i]]
                    #print("tmp1",tmp1)
                    tmp.append(tmp1)
                    print("tmp",tmp)
            #print("s[:i+1]",s[:i+1])
            if s[:i+1] == s[:i+1][::-1] and [s[:i+1]] not in tmp:
                #print("s[:i+1]",s[:i+1])
                tmp.append([s[:i+1]])
            pre = tmp
        return pre
    else:
        return []


def partition(s):
    if not s:
        return [[]]
    tmp =[]
    for i in range(1,len(s)+1):
        if s[:i] ==s[:i][::-1]:
            tmp+=[[s[:i]]+ x for x in partition(s[i:])]
    return tmp

s="efe"
s="dde"
s="bb"
s="abbab"
t=partition(s)
