# dp[n][i][k] 为长度为 n，最大值为 i，search_cost 为 k 的数组的数目,search_cost是递增子序列的长度
# 所求即为sum(i=1—>m)dp[n][i][k]
# 三维DP，只需要找到三个边界情况并初始化就可以了
# 当n = 1时，只有一个位置，k = 1时，结果为1，其余结果都为0
# 当i = 1时，只有一种数可以选，那么 k = 1 时，结果为1, 其余结果都为0
# 当k = 0时，不管 i, j 选什么，结果都是0
# 对于其它的 n, i, k 分两种情况考虑：
# 情况1：当最大值 i 恰好只出现在数组末尾时, 构造的方法有 sum(j=1—>i-1)dp[n−1][j][k−1] 种
# 情况2：而当最大值出现在前 n-1 个元素之中时，数组末尾的元素可以从 1 到 i 中任意选取，即有 i * dp[n-1][i][k]种构造方法．

def numOfArrays(n,m,k):
    if k == 0:
        return 0
    # 多维dp创建时，从内到外创建是对应dp[n][i][k]从尾到头
    dp = [[[0 for _ in range(k + 1)] for _ in range(m + 1)] for _ in range(n + 1)]
    mod = 1000000007
    for j in range(m + 1):
        for p in range(k + 1):
            if p==1:
                dp[1][j][p]=1
            else:
                dp[1][j][p]=0
    for i in range(n + 1):
        for p in range(k + 1):
            if p==1:
                dp[i][1][p] = 1
            else:
                dp[i][1][p] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            dp[i][j][0]=0


    for i in range(2,n + 1):
        for j in range(2,m + 1):
            for p in range(1,k + 1):
                for b in range(1, j):
                    dp[i][j][p] = dp[i][j][p] + dp[i - 1][b][p - 1]
                    dp[i][j][p] = dp[i][j][p] % mod
                dp[i][j][p] = dp[i][j][p] + j * dp[i - 1][j][p]
                dp[i][j][p] = dp[i][j][p] % mod
    res = 0
    for i in range(1, m + 1):
        res += dp[n][i][k]
        res %= mod
    return res
