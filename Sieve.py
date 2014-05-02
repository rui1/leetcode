def sieve(n):
    "Return all primes <= n."
    np1 = n + 1
    s = list(range(np1)) # leave off `list()` in Python 2
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in range(2, sqrtn + 1): # use `xrange()` in Python 2
        if s[i]:
            # next line:  use `xrange()` in Python 2
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return filter(None, s)
def sundaram3(max_n):
    numbers = list(range(3, max_n+1, 2))
    half = (max_n)//2
    initial = 4

    for step in range(3, max_n+1, 2):
        for i in range(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + filter(None, numbers)
def PerfectGen(count, start=0):
    output = 0
    prime  = 0 
    while output < count:
        prime = self.NextPrime(prime)
        mPrime = 2**prime - 1

        if not self.IsPrime(mPrime):
            continue
        
        pN =(2**(prime-1))*(2**prime - 1)
        if pN >= start:
            output += 1
            yield pN
def PrimeGen(count, start):
    c     = 0
    base  = [2,3,5]
    start = int(round(start))
          
    n = (2,max(2,(start,start+1)[start % 2 == 0]))[start != 2]
    
    while c < count:
              
        if n in base:
            yield n
            if n == 2: n+=1; c+=1; continue
            else: n+=2; c+=1; continue
            
        if not [m for m in base if (n%60) % m == 0 ]:
            if n % n**0.5 != 0:
                if self.PrimeFactor(n):
                    c += 1
                    yield n
            n += 2

