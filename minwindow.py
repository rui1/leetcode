class Solution:
    # @return a string
    def minWindow(self, S, T):
        if len(T)>len(S) or S=='' or S is None or T is None or T =='':
            return ''
        if len(T)==len(S)
            if T ==S:
                return S
            else:
                return ''

        best = len(S)+10
        start = end = -1
        hs = [-1]*len(T)
        for i in range(len(S)):
            tmp = T.find(S[i])
            if tmp !=-1:
                hs[tmp]=i
                if -1 not in hs:
                    tstart = min(hs)
                    tend =i
                    if best>tend-tstart:
                        best = tend -tstart
                        start =tstart
                        end = tend
                        print best, start, end
        if start==-1 or end ==-1:
            return ''
        else:
            return S[start:end+1]
            

test = Solution()
print test.minWindow('aa','aa')
