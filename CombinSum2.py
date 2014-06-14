def CombSum2(C,G):
    hs = {}
    for i in range(1,G+1):
        hs[i]=[]
        if i in C:
            cnt = C.count(i)
            k = 0
            start =0
            while k <cnt:
                tmp = C.index(i, start)
                start= tmp +1
                k+=1
                hs[i].append([tmp])
        j = 0
        while j< i:
            print('current j',j, 'current i',i)
            if j in hs and i-j in hs and len(hs[j])>0 and len(hs[i-j])>0 and j !=i-j:
                print('current j in hs',j,'current i-j in hs',i-j)
                for s1 in hs[j]:
                    for s2 in hs[i-j]:
                        tmp1 = s1+s2
                        tmp2 = list(set(tmp1))
                        tmp1.sort()
                        tmp2.sort()
                        print('Not the same','s1',s1,'s2',s2,'tmp1',tmp1,'tmp2',tmp2)
                        if tmp1 == tmp2 and tmp2 not in hs[i]:
                            hs[i].append(tmp1)
            elif j == i-j and j in hs and len(hs[j])>1:
                print('j and i-j are the same', j)
                for s1 in hs[j][:-1]:
                    for s2 in hs[j][1:]:
                        print('s1',s1,'s2',s2)
                        tmp1 = s1+s2
                        tmp2 = list(set(tmp1))
                        tmp1.sort()
                        tmp2.sort()
                        print('tmp1',tmp1,'tmp2',tmp2)
                        if tmp1 == tmp2 and tmp2 not in hs[i]:
                            hs[i].append(tmp1)
                        
            j+=1
        print('hs',hs)
    results = []
    for s in hs[G]:
        tmp = []
        for i in s:
            tmp.append(C[i])
        tmp.sort()
        print('tmp',tmp)
        if tmp not in results:
            results.append(tmp)
            
    return results

a_in = open('CombSum2.txt',encoding = 'utf-8')
test = [x.replace('\n','').split(';') for x in a_in.readlines()]
G1,C1 = ['6','4,4,2,1,4,2,2,1,3']
G = int(G1)
C =[int(x) for x in C1.split(',')]
t=CombSum2(C,G)
            
        
