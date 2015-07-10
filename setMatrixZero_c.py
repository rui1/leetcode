class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        if len(matrix)==0 or len(matrix[0])==0:
            return
        n = len(matrix)
        m = len(matrix[0])
        first_row = False
        first_col = False
        for i in range(0,n):
            if matrix[i][0]==0:
                first_col = True
                break
        if 0 in matrix[0]:
            first_row=True
            
        for i in range(0,n):
            for j in range(0,m):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0
                    print i,j
        print'matrix', matrix, first_row, first_col
        for i in range(1,n):
            if matrix[i][0]==0:
                matrix[i][1:]=[0]*(m-1)
            for j in range(1,m):
                if matrix[0][j]==0:
                    matrix[i][j]=0
                print i,j, matrix
        if first_row:
            matrix[0]=[0]*m
        if first_col:
            for i in range(0,n):
                matrix[i][0]=0
        return