hs={}
def wordBreak(s,d):
    ret=[]
    if s in hs:
        return hs[s]
    if not s:
        return ['']
    for i in range(1, len(s)+1):
        if s[:i] in d:
            tmp=[s[:i]+' '+x for x in wordBreak(s[i:],d)]
            ret+=[x.strip() for x in tmp]
    hs[s]=ret
    return ret

s="catsanddog"
d=["cat", "cats", "and", "sand", "dog"]
hs={}
t=wordBreak(s,d)
