def wordBreak(self, s, dict):
    if s in self.hs:
        return self.hs[s]
    if len(s)==0:
        return True
    for i in range(1,len(s)+1):
        if s[0:i] in dict:
            if self.wordBreak(s[i:],dict):
                return True
    self.hs[s]=False
    return False
