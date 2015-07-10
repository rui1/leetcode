class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        if len(matrix)==0 or len(matrix[0])==0:
            return
        n = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i,j) not in n and matrix[i][j]==0:
                    n.append((i,j))
        for i, j in n:           
            matrix[i]=[0]*len(matrix[0])
            for k in range(len(matrix)):
                matrix[k][j]=0
            print i,j,n
            print 'matrix',matrix
        return
        