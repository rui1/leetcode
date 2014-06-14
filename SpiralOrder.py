def spiralOrder(maxtrix):
    return spiralOrderRec(matrix, 0,0,'R')
def spiralOrderRec(matrix, i, j, d):
    m=len(matrix)
    ret=[]
    if m ==0:
        return ret
    elif len(matrix[0])==0:
        return ret
    else:
        n = len(matrix[0])
        #print(d,n,m)
        if d =='R':
            for k in range(n):
                ret.append(matrix[i][k])
            tmp = matrix[i+1:]
            #print(i,k,tmp,'D')
            ret+=spiralOrderRec(tmp, i,k,'D')
            return ret
        if d =='D':
            for k in range(m):
                ret.append(matrix[k][j])
            tmp = [x[:j] for x in matrix]
            #print(k,j,tmp,'L')
            ret+=spiralOrderRec(tmp, k,j,'L')
            return ret
        if d =='L':
            for k in range(n-1,-1,-1):
                ret.append(matrix[i][k])
            tmp = matrix[:i]
            #print(i,k,tmp,'U')
            ret+=spiralOrderRec(tmp, i,k,'U')
            return ret
        if d =='U':
            for k in range(m-1,-1,-1):
                ret.append(matrix[k][j])
            tmp = [x[j+1:] for x in matrix]
            #print(k,j,tmp,'R')
            ret+=spiralOrderRec(tmp, k,j,'R')
            return ret


matrix = [[0,1],[2,3]]
matrix=[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
matrix=[[7], [6], [9]]
i = j = 0
d = 'R'
t=spiralOrder(matrix)
