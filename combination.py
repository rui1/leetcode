import time
start_time = time.time()
md={}
def comb(n,k):
    if (n,k) in md:
        return md[(n,k)]
    if n==0:
        if k ==0:
            return 1
        else:
            return 0
    if n <k:
        return 0
    ret = comb(n-1,k-1)+comb(n-1,k)
    md[(n,k)]=ret
    return ret
print(comb(700,100))

print (time.time() - start_time, "seconds")
