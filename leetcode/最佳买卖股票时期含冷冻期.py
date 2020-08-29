def maxProfit(prices):
    n = len(prices)
    if not n or n < 2:
        return 0
    dp = [[0, 0] for i in range(n)]  # dp的初始化

    dp[0][0] = 0  # 第0天不持股自然就为0了
    dp[0][1] = -prices[0]  # 第0天持股，那么价格就是-prices[0]了
    # 第1天不持股，要么第0天就不持股，要么就是第0天持股，然后第1天卖出
    dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
    # 第一天持股，要么就是第0天就持股了，要么就是第0天不持股第1天买入持股
    dp[1][1] = max(dp[0][1], dp[0][0] - prices[1])

    for i in range(2, n):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
    return dp[-1][0]