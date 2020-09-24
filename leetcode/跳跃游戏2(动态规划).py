def jump(nums):
    # 一句话解释: 从一个位置跳到它能跳到的最远位置之间的都只需要一步!
    # 同一个位置最找查询到的结果最小
    n = len(nums)
    if n == 1:
        return 0
    dp = [0 for _ in range(n)]
    for i in range(n):
        for j in range(nums[i], 0, -1):
            # 不到0 因为i+0=i 所以对于i其实没有跳跃
            if i + j >= n - 1:
                return dp[i] + 1
            elif dp[i + j] == 0:
                dp[i + j] = dp[i] + 1
            else:
                break
                # 已经更改过不是0，说明之前已经到达过这个点，之前的结果肯定是最小的
                # 而这个点之前的点,肯定也已经被跳到过
nums=[2,3,1,1,4]
print(jump(nums))