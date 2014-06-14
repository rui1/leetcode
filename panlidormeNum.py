def isPalindrome(x):
    if x<0:
        return False
    else:
        l = len(str(x))
        mid = l//2
        for i in range(mid):
            t1=x%(10**(i+1))//(10**i)
            t2= x%(10**(l-i))//(10**(l-i-1))
            #print(i+1,i,mid,mid+i,mid+i-1,t1,t2)
            if t1!=t2:
                return False
        return True
x=1221
'''l = len(str(x))
if l%2:
    mid = l//2
else:
    mid = l//2
for i in range(mid):
    t1=x%(10**(i+1))//(10**i)
    t2= x%(10**(l-i))//(10**(l-i-1))
    print(i+1,i,mid,l-i,l-i-1
          ,t1,t2)'''

