def isOK(i,j,board,n):
    h = board[i]
    if h.count('Q')!=0:
        return False
    v = [x[j] for x in board]
    if v.count('Q')!=0:
        return False
    #d = [board[x][y] for x in range(0,i+n-j) for y in range(j,n)]
    #if d.count('Q')!=0:
    #    return False
    d=0
    while 0<=i+d<n and 0<=j+d<n:
        if board[i+d][j+d]=='Q':
            return False
        d+=1
    d=0
    while 0<=i-d<n and 0<=j+d<n:
        if board[i-d][j+d]=='Q':
            return False
        d+=1
    d=0
    while 0<=i-d<n and 0<=j-d<n:
        if board[i-d][j-d]=='Q':
            return False
        d+=1
    d=0
    while 0<=i+d<n and 0<=j-d<n:
        if board[i+d][j-d]=='Q':
            return False
        d+=1
    return True
def totalNQueensHelper(n):
    board =[['.' for j in range(n) ]for i in range(n)]
    return True

board=['.Q.','...','...']
isOK(2,2,board,3)
    
    
