def jump(nums):
    # 一句话解释: 从一个位置跳到它能跳到的最远位置之间的都只需要一步!
    n = len(nums)
    if n == 1:
        return 0
    dp = [0] * n
    for i in range(n):
        for j in range(nums[i], 0, -1):
            if i + j >= n - 1:
                return dp[i] + 1
            elif dp[i + j] == 0:
                dp[i + j] = dp[i] + 1
            else:
                break
#               已经更改过不是0，说明之前已经到达过这个点，之前的结果肯定是最小的
nums=[2,3,1,1,4]
print(jump(nums))