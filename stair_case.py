class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n <=0:
            return 0
        hs = {}
        hs[1]=1
        hs[2]=2
        for i in range(3,n+1):
            hs[i]=hs[i-1]+hs[i-2]
        return hs[n]