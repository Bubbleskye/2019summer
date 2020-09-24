# 动态规划
# 子序列要求必须是连续的
def maxSubArray(nums) -> int:
    # 状态方程 dp[i]=max(dp[i-1]+nums[i],nums[i])
    # 以nums[i]为末尾的最大子序和
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    dp = []
    dp.append(nums[0])
    for i in range(1, len(nums)):
        dp.append(max(dp[i - 1] + nums[i], nums[i]))
    return max(dp)