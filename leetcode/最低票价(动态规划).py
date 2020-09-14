def mincostTickets(days, costs):
    dp = [0 for _ in range(days[-1] + 1)]  # dp数组，每个元素代表到当前天数最少钱数，为下标方便对应，多加一个 0 位置
    index=0  # 设定一个days指标，是days中元素的索引
    for i in range(1, len(dp)):
        if i != days[index]:  # 若当前天数不是待处理天数，则其花费费用和前一天相同
            dp[i] = dp[i - 1]
        else:
            # 若 i 走到了待处理天数，则从三种方式中选一个最小的
            dp[i] = min(dp[max(0, i - 1)] + costs[0],
                        dp[max(0, i - 7)] + costs[1],
                        dp[max(0, i - 30)] + costs[2])
            index += 1
    return dp[-1]  # 返回最后一天对应的费用即可
days = [1,4,6,7,8,20]
costs = [2,7,15]
print(mincostTickets(days, costs))