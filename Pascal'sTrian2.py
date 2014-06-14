def getRow(rowIndex):
   # if rowIndex ==0:
    #    return [1]
    #else:
    result = [1]
    for i in range(1,rowIndex+1):
        j=1
        tmp =[1]
        pre=result
        print('pre',pre,'tmp',tmp)
        while j<i:
            tmp.append(pre[j-1]+pre[j])
            j+=1
        tmp.append(1)
        result=tmp
        print('result',result)
    return result
t=getRow(3)
