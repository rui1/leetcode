def mediumArray(A,B):
    if len(A)==0 and len(B)!=0:
        mids = Find(findMedian(B),B)
        return sum(mids)/len(mids)
    elif len(B)==0 and len(A)!=0:
        mids = Find(findMedian(A),A)
        return sum(mids)/len(mids)
    elif len(B)==1 and len(A)==1:
        return (B[0]+A[0])/2
    elif len(B)==1 and len(A)>1:
        midI = findMedian(A)[0]
        if B[0]< A[]:
            return mediumArray(A[])
        
def FindMedian(a):
    if len(a)==1:
        return[0]
    else:
        m1 = len(a)//2
        if len(a)%2==0:
            return [m1,m1-1]
        else:
            return [m1]


def Find(arr,l):
    tmp = []
    for i in arr:
        tmp.append(arr[l])
    return tmp
        
