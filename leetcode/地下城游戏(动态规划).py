# 我们希望「从出发点到当前点所需的最小初始值」尽可能小。
# 从右下向左上动态规划
# dp[i][j]为到达坐标（i,j）处的状态值
# 对于 dp[i][j]，我们只要关心 dp[i][j+1] 和 dp[i+1][j] (从坐标到终点所需的最小初始值) 的最小值minn。
# 那么到坐标 (i,j) 所需的状态值要达到 minn−dungeon(i,j) 即可。
# 同时，所有的状态大于等于 1。这样我们就可以得到状态转移方程.
# dp[i][j]=max(min(dp[i+1][j],dp[i][j+1])−dungeon(i,j),1)
def calculateMinimumHP(dungeon):
    rows, cols = len(dungeon), len(dungeon[0])
    dp = [[None for _ in range(cols)] for _ in range(rows)]
    # 先填充最后一格
    if dungeon[-1][-1] > 0:
        dp[-1][-1] = 1
    else:
        dp[-1][-1] = 1 - dungeon[-1][-1]
    # 填充最后一列
    for i in range(rows - 2, -1, -1):
        tmp = dp[i + 1][-1] - dungeon[i][-1]
        if tmp <= 0:
            dp[i][-1] = 1
        else:
            dp[i][-1] = tmp
    # 填充最后一行
    for i in range(cols - 2, -1, -1):
        tmp = dp[-1][i + 1] - dungeon[-1][i]
        if tmp <= 0:
            dp[-1][i] = 1
        else:
            dp[-1][i] = tmp
    for i in range(rows - 2, -1, -1):
        for j in range(cols - 2, -1, -1):
            minn = min(dp[i + 1][j], dp[i][j + 1])
            dp[i][j] = max(minn - dungeon[i][j], 1)
    return dp[0][0]