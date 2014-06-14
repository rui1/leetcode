def isValidSudoku(board):
    use = [list(x) for x in board]
    for i in range(0,9):
        for j in range(0,9):
            if use[i][j]!='.' and not isSafe(use[i][j],i,j,board):
                return False
    return True

def isSafe(num,i,j, board):
    h= board[i]
    v = [x[j] for x in board]
    r = [board[x][y] for x in range(i//3*3,i//3*3+3) for y in range(j//3*3,j//3*3+3)]
    #print(h,v,r)
    #print(h.count(num),v.count(num),r.count(num))
    return h.count(num)==1 and v.count(num)==1 and r.count(num)==1

board=[".....7..9",".4..812..","...9...1.","..53...72","293....5.",".....53..","8...23...","7...5..4.","531.7...."]
t = [list(x) for x in board]
s = isSafe('7',0,5,t)
v = isValidSudoku(board)
