class Solution:
    # @param s, a string
    # @return an integer
    def __init__(self):
        self.hs = {}
    def numDecodings(self, s):
        if s is None or len(s)<1:
            return 0
        if s[0]=='0':
            return 0
        if s in self.hs:
            return self.hs[s]
        if len(s)<2 and int(s)>0:
            return 1
        ret = 0
        if s[:1].isdigit():
            if int(s[:1])>0:
                ret +=self.numDecodings(s[1:])
        if len(s)>1 and s[:2].isdigit():
            if 0<int(s[:2])<27:
                if len(s[2:])>0:
                    ret+=self.numDecodings(s[2:])
                else:
                    ret+=1
        self.hs[s]=ret
        return self.hs[s]        