def longestIncreasingPath(matrix) -> int:
    if not matrix:
        return 0
    direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    dp = [[1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    def backtrack(x, y):
        for dx, dy in direction:
            if 0 <= x + dx < len(matrix) and 0 <= y + dy < len(matrix[0]) and matrix[x + dx][y + dy] < matrix[x][y]:
                if dp[x + dx][y + dy] != 1:
                    dp[x][y] = max(dp[x][y], 1 + dp[x + dx][y + dy])
                else:
                    dp[x][y] = max(dp[x][y], 1 + backtrack(x + dx, y + dy))
        return dp[x][y]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            backtrack(i, j)
    return max(map(max, dp))