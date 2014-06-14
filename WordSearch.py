import copy
#hs={}
class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.existRec(board, word, i,j,set()):
                    return True
        return False
    
    def existRec(self,board, word, i, j,visited):
        if (i,j) in visited:
            return False
        if not word:
            return True
        if i<0 or j<0:
            return False
        if i >len(board)-1 or j >len(board[i])-1:
            return False
        if board[i][j]!=word[0]:
            return False
        elif board[i][j]==word[0]:
            visited.add((i,j))
            if self.existRec(board, word[1:],i-1,j,visited):
                return True
            if self.existRec(board, word[1:],i,j-1,visited):
                return True
            if self.existRec(board, word[1:],i+1,j,visited):
                return True
            if self.existRec(board, word[1:],i,j+1,visited):
                return True
            visited.remove((i,j))
            return False 
        #return hs[(word,i,j)]


board = [
  "ABCE",
  "SFCS",
  "ADEE"
]

word = 'ABCCED'
hs={}
t= exist(board, word)
