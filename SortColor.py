def sortColors1(A):
    hs=[0]*3
    for i in A:
        hs[i]+=1
    return [0]*hs[0]+[1]*hs[1]+[2]*hs[2]

def sortColors(A):
    hs=[0]*3
    for i in A:
        hs[i]+=1
    k = 0
    print(hs)
    for l in range(0,3):
        for j in range(0,hs[l]):
            A[k]=l
            k+=1
    return
A=[0]
