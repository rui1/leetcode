def gray(n):
    start = [0]*n
    hs={1:['0','1']}
    for i in range(1,n+1):
        if i-1 in hs:
            tmp = [ '0'+ str(x) for x in hs[i-1]]
            tmp1 = ['1'+str(x) for x in hs[i-1][::-1]]
            hs[i]=tmp+tmp1
    print(hs)
    ret = []
    for k in hs[n]:
        tmp =0
        #print(k, k[0],k[1])
        for y in range(len(k)):
            tmp+=int(k[y])*2**(len(k)-1-y)
            #print(k,y,k[y],tmp)
            #print(int(k[y])**(len(k)-1-y))
        ret.append(tmp)
    
    return ret


n=1
