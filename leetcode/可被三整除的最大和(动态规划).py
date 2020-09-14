def maxSumDivThree(nums):
    dp0 = [0 for _ in range(len(nums))]
    dp1 = [float("-inf") for _ in range(len(nums))]
    dp2 = [float("-inf") for _ in range(len(nums))]
    if nums[0] % 3 == 0:
        dp0[0] = nums[0]
    elif nums[0] % 3 == 1:
        dp1[0] = nums[0]
    else:
        dp2[0] = nums[0]

    for i in range(1, len(nums)):
        if nums[i] % 3 == 0:
            dp0[i] = max(dp0[i - 1] + nums[i], nums[i])
            dp1[i] = max(dp1[i - 1], dp1[i - 1] + nums[i])
            dp2[i] = max(dp2[i - 1], dp2[i - 1] + nums[i])
        elif nums[i] % 3 == 1:
            dp0[i] = max(dp0[i - 1], dp2[i - 1] + nums[i])
            dp1[i] = max(dp1[i - 1], dp0[i - 1] + nums[i])
            dp2[i] = max(dp2[i - 1], dp1[i - 1] + nums[i])
        else:
            dp0[i] = max(dp0[i - 1], dp1[i - 1] + nums[i])
            dp1[i] = max(dp1[i - 1], dp2[i - 1] + nums[i])
            dp2[i] = max(dp2[i - 1], dp0[i - 1] + nums[i])

    return dp0[-1]


nums=[2,19,6,16,5,10,7,4,11,6]
print(maxSumDivThree(nums))
# dp0[i]是，到第nums[i]个数时，去若干数除以三取余是0的最大的和
# 重点在于dp0用0初始化，因为dp[0]=0 因为0%3=0
# dp[1]dp[2]都设置极限值相当于这个地方的值还是空的，还没有合适的值填入，如果设为0，则会影响最终结果