import time
start_time= time.time()
def multiplicity(n,p):
    if p>n:
        return 0
    if p>n//2:
        return 1
    q,m=n,0
    while q>=p:
        q//=p
        m+=q
    return m

def primes(n):
    n =n+1
    sieve=list(range(n))
    sieve[:2]=[0,0]
    for i in range(2,int(n**0.5)+1):
        if sieve[i]:
            for j in range(i**2,n,i):
                sieve[j]=0
    return[p for p in sieve if p]

def powproduct(ns):
    if not ns:
        return 1
    units = 1
    multi = []
    for base, exp in ns:
        if exp ==0:
            continue
        elif exp ==1:
            units*=base
        else:
            if exp%2:
                units*=base
            multi.append((base, exp//2))
    return units*powproduct(multi)**2
#ns = [(p,multiplicity(10,p)) for p in primes(10)]
def fact(n):
    return powproduct((p,multiplicity(n,p)) for p in primes(n))
#t=fact(100)
def factorN(n):
    ret = 1
    for i in range(1,n+1):
        ret*=i
    return ret
#factorN(100)
#multiplicity(100,13)
#primes(100)

def factor(n):
    if n<=1100:
        return factorN(n)
    else:
        return fact(n)

def num_zeros(n):
    return multiplicity(n,5)
tic = time.time()
#factor(100000)
print(factor(100))
print(num_zeros(100))
print(time.time()-tic, "second")
