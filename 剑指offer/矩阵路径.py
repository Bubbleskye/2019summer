# def exist(board, word) :
#     rows = len(board)
#     cols = len(board[0])
# 
#     def backtrack(i, j, word,board,flag):
#         if len(word) == 0:
#             return True
#         if i<0 or j<0 or i>= len(board) or j>= len(board[0]) or flag[i][j] == 1 or word[0] != board[i][j]:
#             return False
#         flag[i][j]=1
#         if backtrack(i-1, j, word[1:],board,flag) or backtrack(i+1, j, word[1:],board,flag) or backtrack(i, j-1,  word[1:],board,flag) or backtrack(i, j+1,  word[1:],board,flag):
#             return True
#         flag[i][j] = 0
#         return False
# 
#     flag = [[0 for _ in range(cols)] for _ in range(rows)]
#     for i in range(rows):
#         for j in range(cols):
#             if backtrack(i, j, word,board,flag):
#                 return True
#     return False

def hasPath(matrix, rows, cols, path):
    # write code here
    def backtrack(i, j, path, matrix, rows, cols, flag):
        if len(path) == 0:
            return True
        if i < 0 or j < 0 or i > rows - 1 or j > cols - 1 or flag[i][j] == 1 or path[0] != matrix[i][j]:
            return False
        flag[i][j] = 1
        if backtrack(i - 1, j, path[1:], matrix, rows, cols, flag) or backtrack(i + 1, j, path[1:], matrix, rows, cols,flag) or backtrack(i , j-1, path[1:], matrix, rows, cols,flag) or backtrack(i , j+1, path[1:], matrix, rows, cols,flag):
            return True
        flag[i][j] = 0
        return False

    flag = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if backtrack(i, j, path, matrix, rows, cols, flag):
                return True
    return False

matrix=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
rows=3
cols=4
path="ABCCED"
print(hasPath(matrix, rows, cols, path))