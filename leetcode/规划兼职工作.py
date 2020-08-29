def jobScheduling(startTime, endTime, profit):
    n = len(profit)
    idx = sorted(list(range(n)), key=lambda x: endTime[x])
    # 按结束时间排序
    dp = [[0, 0] for _ in range(n + 1)]
    # dp到当前任务时，最大的利润以及结束的时间（因为按结束时间排序，所以在利润相同时，选择靠前的，因为结束时间靠前）
    # 可以用一个数组记录在每一个结束时间处可以得到的最大利润。dp[0]得到的最大利润/dp[1]结束时间
    for i in range(n):
        for j in range(i, -1, -1):
            if dp[j][1] <= startTime[idx[i]]:
                cur = dp[j][0] + profit[idx[i]]
                # cur是包含当前i任务，那么最大利润就是当前利润，加上结束时间在当前任务开始时间之前的最大利润
                break
        if dp[i][0] >= cur:
            dp[i + 1] = dp[i]
        #如果不包含当前任务利润更大，那么最大利润就是前一个最大利润
        else:
            dp[i + 1]=[cur, endTime[idx[i]]]
    return dp[-1][0]


startTime=[1,2,3,4,6]
endTime=[3,5,10,6,9]
profit=[20,20,100,70,60]
print(jobScheduling(startTime, endTime, profit))