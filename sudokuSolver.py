def isSafe(num,i,j, board):
    h= board[i]
    if h.count(num)!=0:
        return False
    v = [x[j] for x in board]
    if v.count(num)!=0:
        return False
    r = [board[x][y] for x in range(i//3*3,i//3*3+3) for y in range(j//3*3,j//3*3+3)]
    if r.count(num)!=0:
        return False
    return True
def solveSudokuhelper(board):
    for i in range(9):
        for j in range(9):
            if board[i][j]=='.':
                for k in range(1,10):
                    num = str(k)
                    if isSafe(num, i,j,board):
                        board[i][j]= num
                        if solveSudokuhelper(board):
                            return True
                        else:
                            board[i][j]="."
                return False
    return True
def solveSudoku(board):
    for row in range(9):
        board[row] = list(board[row])
    solveSudokuhelper(board)

board=[".....7..9",".4..812..","...9...1.","..53...72","293....5.",".....53..","8...23...","7...5..4.","531.7...."]
solveSudoku(board)

