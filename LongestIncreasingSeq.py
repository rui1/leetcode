def LIS(s):
    hs = {}
    for i in range(len(s)):
        hs[i]=1
    for i in range(1,len(s)):
        for j in range(0,i):
            if s[i]>s[j] and hs[i]<hs[j]+1:
                hs[i]=hs[j]+1
                print(hs)
    return max(hs.values())

s = [10,22,9,33,21,50,41,60,80]

def LIS_out(s):
    hs = {}
    for i in range(len(s)):
        hs[i]=[1,i]
    for i in range(1,len(s)):
        for j in range(0,i):
            if s[i]>s[j] and hs[i][0]<hs[j][0]+1:
                hs[i][0]=hs[j][0]+1
                hs[i][1]=j
                print(hs)
    mx = 0
    for k in hs:
        if hs[k][0]>mx:
            mx = hs[k][0]
    res= []
    while k in hs and k !=hs[k][1]:
        res.append(s[k])
        k=hs[k][1]
    res.append(s[k])
    return res

