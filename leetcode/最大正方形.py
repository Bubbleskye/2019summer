def maximalSquare(matrix):
    row = len(matrix)
    if row == 0:
        return 0
    col = len(matrix[0])
    marked = [[0 for _ in range(col)] for _ in range(row)]
    for i in range(row):
        if matrix[i][0] == "1":
            marked[i][0] = 1
    for i in range(col):
        if matrix[0][i] == "1":
            marked[0][i] = 1
    for i in range(1, row):
        for j in range(1, col):
            if matrix[i][j] == "1":
                marked[i][j] = min(marked[i - 1][j], marked[i][j - 1], marked[i - 1][j - 1]) + 1
    return max(map(max, marked)) ** 2

#  dp(i, j)表示以 (i,j) 为右下角，且只包含 1 的正方形的边长最大值
# 如果我们能计算出所有dp(i,j) 的值，那么其中的最大值即为矩阵中只包含 1 的正方形的边长最大值，其平方即为最大正方形的面积。
# 如果该位置的值是 0，则 dp(i, j) = 0，因为当前位置不可能在由 1 组成的正方形中；
#
# 如果该位置的值是 1，则 dp(i, j) 的值由其上方、左方和左上方的三个相邻位置的 dp 值决定。
# 具体而言，当前位置的元素值等于三个相邻位置的元素中的最小值加 11，状态转移方程如下：
# dp(i,j)=min(dp(i−1,j),dp(i−1,j−1),dp(i,j−1))+1
matrix=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(maximalSquare(matrix))