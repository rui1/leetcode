class Solution:
    # @return an integer
    def __init__(self):
        self.hs = {}
    def minDistance(self, word1, word2):
        if len(word1)==0:
            return len(word2)
        if len(word2)==0:
            return len(word1)
        if (word1,word2) in self.hs:
            return self.hs[(word1,word2)]
        if word1[0]==word2[0]:
            self.hs[(word1,word2)]=self.minDistance(word1[1:],word2[1:])
        if word1[0]!=word2[0]:
            self.hs[(word1,word2)]=min(1+self.minDistance(word1[1:],word2[1:]),1+self.minDistance(word1,word2[1:]),1+self.minDistance(word1[1:],word2))
        return self.hs[(word1,word2)]