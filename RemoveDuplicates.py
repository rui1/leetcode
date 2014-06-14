def removeDuplicates(A):
    if len(A)==0:
        return 0
    else:
        cur = A[0]
        cnt =len(A)
        i=1
        while i<len(A):
            print('i',i)
            if A[i]==cur:
                print('same','current A',A[i])
                A = A[:i]+A[i+1:]
                cnt-=1
                i+=0
                print('cur',cur,'cnt',cnt,'A',A,'next i',i)
            else:
                #print('new','curent A',A[i])
                cur = A[i]
                i+=1
                #print('cur',cur,'cnt',cnt,'A',A,'next i',i)
        return cnt
    
a=[1,1,2,2,2,2,3,3,3,4,4,5,6,7,8,8]
def removeDuplicates_1(A):
    if A is None or len(A)==0:
        return 0
    else:
        cur = A[0]
        cnt =0
        i=1
        for i in range(1,len(A)):
            if A[i]!=A[i-1]:
                cnt+=1
                A[cnt]=A[i]
            print('A',A,'cnt',cnt)

        return cnt+1
    
