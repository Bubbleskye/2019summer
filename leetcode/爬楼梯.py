def climbStairs(self, n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2

    dp = [0, 1, 2]
    for i in range(3, n):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n - 1] + dp[n - 2]

#用递归的方法会导致超时
#这里采用动态规划,自下而上解决问题,将子子问题的答案都存在列表中,方便最后取用,避免了重复计算.