def permute(num):
    return permuteRec(num)
def permuteRec(num):
    if not num:
        return [[]]
    else:
        ret =[]
        for i in range(len(num)):
            tmp = num[:]
            tmp.remove(num[i])
            rest = permuteRec(tmp)
            for j in range(len(rest)):
                rest[j].append(num[i])
                ret.append(rest[j])
        return ret

num=[1,2,3]
t=permute(num)
