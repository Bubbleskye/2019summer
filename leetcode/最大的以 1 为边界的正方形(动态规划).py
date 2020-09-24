# 正方形里面可以有0
def largest1BorderedSquare(grid):
    row = len(grid)
    col = len(grid[0])
    # top[i][j]以[i,j]为以右下角的正方形的上方有多少个连续的1
    # left[i][j]以[i,j]为以右下角的正方形的左边有多少个连续的1
    top = [[0 for _ in range(col)] for _ in range(row)]
    left = [[0 for _ in range(col)] for _ in range(row)]
    maxlen = 0
    # 初始化
    if grid[0][0] == 1:
        top[0][0] = 1
        left[0][0] = 1
        maxlen = max(maxlen, 1)
    for i in range(1, row):
        if grid[i][0] == 1:
            top[i][0] = top[i - 1][0] + 1
            left[i][0] = 1
            maxlen = max(maxlen, 1)
    for j in range(1, col):
        if grid[0][j] == 1:
            top[0][j] = 1
            left[0][j] = left[0][j - 1] + 1
            maxlen = max(maxlen, 1)

    for i in range(1, row):
        for j in range(1, col):
            if grid[i][j] == 1:
                top[i][j] = top[i - 1][j] + 1
                left[i][j] = left[i][j - 1] + 1
                # 找到以[i,j]为以右下角的正方形的上方和左方连续1的最小值k
                # 再去检查，向上找k个位置之后的点的左边连续的1是否满足条件
                # 再去检查，向左找k个位置之后的点的上边连续的1是否满足条件
                for k in range(min(top[i][j], left[i][j]), 0, -1):
                    if top[i][j - k + 1] >= k and left[i - k + 1][j] >= k:
                        maxlen = max(maxlen, k)
    return maxlen * maxlen

grid = [[1,1,1],[1,0,1],[1,1,1]]
print(largest1BorderedSquare(grid))