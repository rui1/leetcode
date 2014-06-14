def generate(numRows):
    result = []
    result.append([1])
    l=0
    r=0
    for i in range(1,numRows):
        j=1
        tmp =[1]
        pre=result[i-1]
        while j<i:
            tmp.append(pre[j-1]+pre[j])
            j+=1
        tmp.append(1)
        result.append(tmp)
        print('pre',pre,'tmp',tmp)
    return result


def merge(A, m, B, n):
    i=0
    for j in B:
        while i<len(A) and A[i]<j:
            i+=1
        if i<len(A):
            A[i+1:]=A[i:]
            A[i]=j
        else:
            A.append(j)
    return
A = [1,3,4,5,6,9]
B=[2,4,7,10]
C=[]
d=[1]
