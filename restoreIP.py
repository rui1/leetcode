class Solution:
    # @param s, a string
    # @return a list of strings
    def __init__(self):
        self.hs={}
    def restoreIpAddresses(self, s):
        ret=[]
        if len(s)>12 or len(s)<4:
            return ret
        
        for i in range(len(s)-2):
            first = s[:i+1]
            if not self.isValid(first):
                continue
            for j in range(i+1, len(s)-1):
                second = s[i+1:j+1]
                if not self.isValid(second):
                    continue
                for k in range(j+1, len(s)):
                    third = s[j+1:k+1]
                    forth = s[k+1:]
                    if not self.isValid(third) or not self.isValid(forth):
                        continue
                    tmp = first+'.'+second+'.'+third+'.'+forth
                    ret.append(tmp)
        return ret
                    
    def isValid(self,s):
        if len(s)>1 and s[0]=='0':
            return False
        if s.isdigit() and 0<= int(s)<=255:
            return True
        return False

test = Solution()
print test.restoreIpAddresses("0000")
print test.isValid('0')
