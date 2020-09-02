# dp[i][j]表示在nums坐标[i, j]中，先手比后手最多多出来的分数
# 情况一：A选择nums[i]。然后轮到另一个玩家B在数组剩下的部分选取数字，B成了[i+1…j]游戏中的先手，此时B和A之间的分差为 dp[i+1][j]
# dp[i+1][j]-nums[i] 是坐标[i, j]B与A的差 所以A先手与B的差是dp[i][j]=-(dp[i+1][j]-nums[i])=nums[i]-dp[i+1][j]
# 情况二：A选择nums[j]。然后轮到另一个玩家B在数组剩下的部分选取数字，B成了[i…j−1]游戏中的先手，此时B和A之间的分差为 dp[i][j-1]
# dp[i][j-1]-nums[j] 是坐标[i, j]B与A的差 所以A先手与B的差是dp[i][j]=-(dp[i][j-1]-nums[j]])=nums[j]-dp[i][j-1]
# 所以dp[i][j]=max(nums[i]-dp[i+1][j],nums[j]-dp[i][j-1])

def PredictTheWinner(nums):
    if not nums:
        return False
    dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
    for i in range(len(nums)):
        dp[i][i] = nums[i]
    for i in range(len(nums) - 2, -1, -1):
        for j in range(i + 1, len(nums)):
            dp[i][j] = max(nums[j] - dp[i][j - 1], nums[i] - dp[i + 1][j])
    return dp[0][-1] >= 0