def lengthOfLIS(nums):
    if not nums:
        return 0
    dp = [1 for _ in range(len(nums))]
    for i in range(len(nums)):
        for j in range(0, i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[j] + 1, dp[i])
    return max(dp)

# 动态规划 状态转移方程 dp[i] = max(dp[j] + 1, dp[i])
# 以i为末尾的字符串中，最长字串的长度是，遍历i之前的所有nums，如果比nums[i]小，则在dp[i]+1，最后取所有的max，作为dp[i]