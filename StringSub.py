def StringSub(file):
    a_in = open(file,'r')
    content =[x.replace('\n','').strip().split(';') for x in a_in.readlines()]
    for i in content:
        s,sb = i
        sd =sb.split(',')
        #print(s,sd)
        fixed=[]
        for j in list(range(0, len(sd),2)):
            #print('cuttnet j',j)
            #print('current',sd[j])
            start = 0
            k = 0
            cnt = s.count(sd[j])
            #print('cnt',cnt)
            while k <cnt:
                tmp = s.find(sd[j],start)
                start = tmp+len(sd[j+1])
                #print ('tmp',tmp,'start',start)
                if tmp not in fixed and start-1 not in fixed:
                    s = s[:tmp]+sd[j+1]+s[tmp+len(sd[j]):]
                    for f in range(*[tmp, start]):
                        fixed.append(f)
                        k+=1
                    #print('REPLACE',s,'fixed is',fixed)
                else:
                    k+=1
                
        print (s)
a_in = open('StringSub_Test.txt','r')
content =[x.replace('\n','').strip().split(';') for x in a_in.readlines()]
for i in content:
    s,sb = i
    sd =sb.split(',')
    print(s,sd)
    fixed=[]
    for j in list(range(0, len(sd),2)):
        print('cuttnet j',j)
        print('current',sd[j])
        start = 0
        k = 0
        cnt = s.count(sd[j])
        nxt =0
        print('cnt',cnt)
        while k <cnt:
            tmp = s.find(sd[j],nxt)            
            start = tmp+len(sd[j+1])
            print ('tmp',tmp,'start',start)
            if tmp not in fixed and start-1 not in fixed:
                s = s[:tmp]+sd[j+1]+s[tmp+len(sd[j]):]
                nxt = start
                for f in range(*[tmp, start]):
                    fixed.append(f)
                    k+=1
                    if max(fixed)>f and len(sd[j])!=len(sd[j+1]):
                        idxs = [fixed.index(x) for x in fixed if x > f]
                        for idx in idxs:
                            fixed[idx]+=len(sd[j+1])-len(sd[j])
                print('REPLACE',s,'fixed is',fixed)
            else:
                k+=1
                nxt = tmp+1
    print (s)


StringSub("StringSub_Test.txt")
