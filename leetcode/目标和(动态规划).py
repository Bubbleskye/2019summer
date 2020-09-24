# nums=[20,48,33,16,19,44,14,31,42,34,38,32,27,7,22,22,48,18,48,39]
# S=1
# if not nums:
#     print(0)
# direction = [-1, 1]
# global count
# count=0
# def drawback(nums, ssum):
#     global count
#     if len(nums) == 0 and ssum == S:
#         count=count+1
#     if len(nums)==0:
#         return
#     for d in direction:
#         drawback(nums[1:], ssum + d * nums[0])
#
# ssum = 0
# for d in direction:
#     drawback(nums[1:], ssum + d * nums[0])
# print(count)
# 回溯超时

nums=[7,9,3,8,0,2,4,8,3,9]
S=0
def findTargetSumWays(nums , S):
    if not nums:
        return 0
    if len(nums) == 1 and S != nums[0] and S != -nums[0]:
        return 0
    if len(nums) == 1 and S == nums[0]:
        return 1
    ssum = sum(nums)
    if S > ssum or S < -ssum:
        return 0
    # dp[i][j] 表示用数组中的前 i 个元素，组成和为 j 的方案数
    dp = [[0 for _ in range(0, 2 * ssum + 1)] for _ in range(len(nums))]
    # 初始化 到第i个位置和为sum(nums[:i+1])的方案有1种
    for i in range(len(nums)):
        if nums[i]!=0:
            dp[i][sum(nums[0:i + 1]) + ssum] = 1
            dp[i][-sum(nums[0:i + 1]) + ssum] = 1
        else:
            # 如果nums[i]==0，则0有正负两种选择达到sum(nums[0:i + 1])，所以是2
            dp[i][sum(nums[0:i + 1]) + ssum] = 2
            dp[i][-sum(nums[0:i + 1]) + ssum] = 2
    # dp[i][j] = dp[i - 1][j - nums[i]] + dp[i - 1][j + nums[i]]
    # 到第i个位置,和为j的个数=到第i-1个位置,和为j-nums[i],相当于nums[i]前是+号  +   到第i-1个位置,和为j+nums[i],相当于nums[i]前是-号
    for i in range(1, len(nums)):
        for j in range(-ssum, ssum + 1, 1):
            dp[i][j] = dp[i - 1][j - nums[i]] + dp[i - 1][j + nums[i]]
    return dp[-1][S + ssum]

# dp[i][j] = dp[i - 1][j - nums[i]] + dp[i - 1][j + nums[i]]
print(findTargetSumWays(nums , S))