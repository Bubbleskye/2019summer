def maxProfit(prices):
    if not prices:
        return 0
    dp = [0 for _ in range(len(prices))]
    minprice = prices[0]
    for i in range(1, len(prices)):
        dp[i] = max(dp[i - 1], prices[i] - minprice)
        minprice = min(minprice, prices[i])
    return dp[-1]