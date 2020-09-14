def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    dp = [0 for _ in range(len(nums))]
    # 到第i家为止的最大金额
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
    return dp[-1]

nums=[2,7,9,3,1]
print(rob(nums))