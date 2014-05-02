def singleNumber(self, A):
    bit= [0]*64
    for i in A:
        for j in range(len(bit)):
            if i & 1<<j == 1<<j:
                bit[j]+=1
        
    res = 0
    if bit[31] % 3 == 0: # posivie
        for i in xrange(31): 
            if bit[i] % 3 == 1: res += 1 << i    
    else: # negative
        for i in xrange(31): 
            if bit[i] % 3 == 0: res += 1 << i
        res = -(res + 1)
    return res
