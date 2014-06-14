def dbyd_int(N):
    ds = len(str(N))
    l = []
    rest =N
    print(rest)
    for i in range(ds,0,-1):
        print('i',i)
        hd=0
        k =0
        ak=0
        if len(l)>0:   
            for j in range(len(l)):
                hd+=2*(l[j]*10**(ds-1-j))
        print('hd',hd)
        tmp=hd
        while rest-tmp>=0 and k <10:
            print(rest-tmp)
            tmp=hd
            t=k*(10**(i-1))
            tmp *=t
            tmp+=t**2
            ak=k
            k+=1
            print('tmp',tmp,'k',k,'ak',ak,'t',t)
        ad=max(0,ak-1)
        l.append(ad)
        rest-=hd*ad*(10**(i-1))+(ad*(10**(i-1)))**2
        print('l',l,'rest',rest)
        
    return int(''.join(map(str,l)))
             
def dbyd_dec(N):
    ds = len(str(N))
    l = []
    rest =N
    #print(rest)
    for i in range(ds,-8,-1):
        #print('i',i)
        hd=0
        k =0
        ak=0
        if len(l)>0:   
            for j in range(len(l)):
                hd+=2*(l[j]*10**(ds-1-j))
                print('hd add',2*(l[j]*10**(ds-1-j)),'power',ds-1-j)
        #print('hd',hd)
        tmp=0
        while rest-tmp>=0 and k <10:
            print(rest-tmp)
            tmp=hd
            t=k*(10**(i-1))
            tmp *=t
            tmp+=t**2
            ak=k
            k+=1
            #print('tmp',tmp,'k',k,'ak',ak,'t',t)
        ad=max(0,ak-1)
        l.append(ad)
        rest-=hd*ad*(10**(i-1))+(ad*(10**(i-1)))**2
        #print('l',l,'rest',rest)
        
    return float(''.join(map(str,l[:ds]))+'.'+''.join(map(str,l[ds:])))
  
        
        
N=53361
N=49
N=2
t=dbyd_dec(N)
