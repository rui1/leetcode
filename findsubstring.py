import re
import itertools
class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S,L):
        ret=[]
        if S is None or L is None or len(S) ==0 or len(L)==0:
            return ret
        words = set(L)
        l= len(L[0])
        total = l*len(L)
        L.sort()
        for start in range(len(S)-total+1):
            sub = S[start:start+l]
            if sub not in words:
                continue
            end = start+total
            tmp=[]
            for j in range(start, end,l):
                sub = S[j:j+l]
                if sub not in words:
                    continue
                tmp.append(sub)
            tmp.sort()
            if tmp==L:
                ret.append(start)
        return ret



    def findSubstring_slow(self, S, L):
        ret=[]
        subs = set(itertools.permutations(L))
        for i in subs:
            tmp =''.join(list(map(str, i)))
            print 'tmp',tmp
            tret = [m.start() for m in re.finditer(tmp, S)]
            print tret
            #ret += [m.start() for m in re.finditer(tmp, L)]
            ret +=tret
        return set(ret)
test = Solution()
print test.findSubstring("barfoothefoobarman",["foo","bar"])
