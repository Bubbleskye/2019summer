def maxSumDivThree(nums):
    dp = [0, -10005, -10005]
    for i in range(len(nums)):
        mod = nums[i] % 3

        c0 = dp[(0 - mod + 3) % 3]
        c1 = dp[(1 - mod + 3) % 3]
        c2 = dp[(2 - mod + 3) % 3]

        c_dp0 = dp[0]
        c_dp1 = dp[1]
        c_dp2 = dp[2]

        dp[0] = max(c_dp0, c0 + nums[i])
        dp[1] = max(c_dp1, c1 + nums[i])
        dp[2] = max(c_dp2, c2 + nums[i])
    return dp[0]
nums=[2,19,6,16,5,10,7,4,11,6]
print(maxSumDivThree(nums))
# dp[i]是，到第i个数时，去若干数除以三取余分别是0，1，2的最大的和
# 重点在于一个一个更新
# dp[0]=0 因为0%3=0
# dp[1]dp[2]都设置极限值相当于这个地方的值还是空的，还没有合适的值填入
# 如果设为0，则会影响最终结果