class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)
        if n <=1:
            return matrix
        if n>1 and n%2:
            mid1= n//2-1
            mid2 = n//2
        else:
            mid1=mid2= n//2-1
        for i in range(0, mid1+1):
            for j in range(0, mid2+1):
                if n-1 -i ==i and n-1-j ==j:
                    continue
                tmp = [matrix[i][j]]
                ti = i
                tj = j
                for k in range(3):
                    #print("this",ti,tj)
                    tmp.append(matrix[tj][n-1-ti])
                    tmpi = ti 
                    tmpj = tj 
                    ti = tmpj
                    tj = n-1-tmpi
                    #print("after rotate", ti, tj)
                    matrix[ti][tj]=tmp[k]
                    #print "matrix", matrix
                #print tmp
                matrix[i][j]=tmp[-1]
        return matrix