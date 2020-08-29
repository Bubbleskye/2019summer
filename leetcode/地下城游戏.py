# 我们希望「从出发点到当前点的路径和」尽可能大，而「从出发点到当前点所需的最小初始值」尽可能小。这两条路径各有优劣。
# 如果按照从左上往右下的顺序进行动态规划，我们无法直接确定到达右下角的方案，因为有两个重要程度相同的参数同时影响后续的决策。
# 于是我们考虑从右下往左上进行动态规划。令 dp[i][j]表示从坐标 (i,j)到终点所需的最小初始值。
# 换句话说，当我们到达坐标 (i,j) 时，如果此时我们的路径和不小于 dp[i][j]，我们就能到达终点。
# 这样一来，我们就无需担心路径和的问题，只需要关注最小初始值。
# 对于 dp[i][j]，我们只要关心 dp[i][j+1] 和 dp[i+1][j] (从坐标到终点所需的最小初始值) 的最小值minn。
# 那么在坐标 (i,j) 的初始值只要达到 minn−dungeon(i,j) 即可。同时，初始值还必须大于等于 1。这样我们就可以得到状态转移方程.
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
