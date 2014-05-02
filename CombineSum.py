def CombineSum(C, G):
    hs = {}
    for i in range(1,G+1):
        hs[i]=[]
        if i in C:
            hs[i].append([i])
        j = 0
        while j<i:
            #print('current j',j, 'current i',i)
            if j in hs and i-j in hs and len(hs[j])>0 and len(hs[i-j])>0:
                #print('current j in hs',j,'current i-j in hs',i-j)
                for s1 in hs[j]:
                    for s2 in hs[i-j]:
                        tmp = s1+s2
                        tmp.sort()
                        if tmp not in hs[i]:
                            hs[i].append(tmp)
            j+=1
        #print('hs',hs)
    return hs[G]

a_in = open('CombinSum.txt',encoding = 'utf-8')
test = [x.replace('\n','').split(';') for x in a_in.readlines()]
G1,C1 = test[1]
G = int(G1)
C =[int(x) for x in C1.split(',')]
t=CombineSum(C,G)
