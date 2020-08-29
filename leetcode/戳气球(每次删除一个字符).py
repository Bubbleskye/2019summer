# 首先我们尝试每戳破一个气球，以该气球为边界将气球数组分为两部分，使用这两部分的解来求解原问题。
# 我们设戳破区间 i 到 j 间的气球我们得到的最大金币数为coin。及coin = def( i , j )。
# 则当我们戳破气球 k 时，两边区间的最大值分别是 def( i , k-1 ) 与 def( k+1 , j )。
# 此时我们发现了问题，因为戳破了气球 k ，气球数组的相邻关系发生了改变，k-1 与 k+1 原本都与 k 相邻，而 k 戳破后他们两个直接相邻了。
# 而且先戳破 k+1 与先戳破 k-1 得到的结果将完全不同，也就是说两个子问题间发生了依赖。
# 如果先戳破 k-1 ，则 k+1 左边的相邻气球变成了 k-2；反之 k-1 右边相邻的气球变成了 k+2 。
# 子问题的处理顺序将影响到每个子问题的解，这将使我们的状态转移方程极为复杂和低效，我们应当换一种划分子问题的方式，使每个子问题都是独立的。
# 那么我们换一种划分方式，既然两个子问题都依赖 k 和两个边界，
# 那么我们划分子问题时，k 与两个边界的气球我们都不戳破，求出 i+1 到 k-1 与 k+1到 j-1 之间的解。
# 这样两个子问题间的依赖便被消除了，两个边界及气球 k 不被戳破，两个子问题的依赖都不会越过 k 到另一个子问题上，子问题间是相互独立的。
# 并且在两个子问题解决后，气球序列还剩下 k 与两个边界的气球没有戳破，那么我们用两个子问题的解与戳破 k 与两个边界的最大值即可求出原问题的解。
# 那么 dp[i , j]定义则为，不戳破 i 与 j ，仅戳破 i 与 j 之间的气球我们能得到的最大金币数。
# 如此划分，状态转移方程为： dp[i,j] = dp[i,k] + dp[k,j]+nums[ i ][ j ][ k ]
# 其中 nums[ i ][ j ][ k ] 为戳破气球 k 时我们能得到的金币数
# k 的取值应当介于 i+1 与 j-1 之间，我们尝试所有 k 的取值并从中挑选最大值，这才是原问题真正的解。
# 真正的状态转移方程应该为：dp[i , j] = max { dp[i , k] + dp[k , j]+nums[ i ][ j ][ k ] }       i<k<j
# 因为 k 是介于 i 与 j 之间的，那么当 i 与 j 相邻时我们的问题将不能再继续划分。此时按照我们对问题的定义，“不戳破 i 与 j ，仅戳破 i 与 j 之间的气球”，因为 i 与 j 之间没有气球，我们得到的金币数是 0 。

def maxCoins(nums):
    nums = [1] + nums + [1]
    # 加了1之后，符合两端的不戳 实际的都可以戳
    n = len(nums)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    # for right in range(2, len(nums)):
    #     for left in range(right - 2, -1, -1):
    #         # 因为 k 是介于 i 与 j 之间的，那么当 i 与 j 相邻时我们的问题将不能再继续划分。所以+2
    #         for i in range(left + 1, right):
    #             dp[left][right] = max(dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
    # 因为从小区间才能计算到大区间，所以从末尾开始
    for left in range(n - 3, -1, -1):
        for right in range(left + 2, n):
            # 因为 k 是介于 i 与 j 之间的，那么当 i 与 j 相邻时我们的问题将不能再继续划分。所以+2
            for i in range(left + 1, right):
            # same formula to get the best score from (left, right) as before
                dp[left][right] = max(dp[left][right],nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right] )
    return dp[0][n - 1]