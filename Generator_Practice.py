def double(L):
    for x in L:
        yield x*2

t= double([1, 2, 3, 4, 5])
def combinations(items,k):
    if k==0: yield []
    else:
        for i in range(len(items)):
            for cc in combinations(items[i+1:],k-1):
                yield [items[i]]+cc

s =list(combinations(list(range(1,5)),2))
