def pow(x, n):
    if n==0:
        return 1
    elif x==0:
        return 0
    elif x==1:
        return 1
    elif x==-1:
        return (-1)**(abs(n)%2)
    elif n>0:
        print("n>0")
        tmp = 1
        k=0
        while k<n:
            tmp*=x
            if abs(tmp)<10e-20:
                return 0
            print(tmp)
            k+=1
        return tmp
    elif n<0:
        print('n<0')
        tmp = 1
        i=0
        while i<abs(n):
            tmp=tmp/x
            if abs(tmp)<10e-20:
                return 0
            i+=1
        return tmp
def pow1(x,n):
    if n<0:
        return 1.0/pow_fast(x,abs(n))
    else:
        return pow_fast(x,n)
def pow_fast(x,n):
    if n ==0:
        return 1
    tmp = pow_fast(x,n//2)
    if n%2==1:
        return tmp*tmp*x
    else:
        return tmp*tmp

x,n = [34.00515, -3]
x,n=[-13.62608,3]
#x,n = [-1.00000,-2147483648]
pow1(x,n)

