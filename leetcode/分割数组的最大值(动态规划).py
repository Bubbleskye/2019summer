# 状态定义：f[i][j]表示前i个数（到nums[i-1]）划分为j组的的最大连续子数组和的最小值。
# 可初始化的状态：f[i][1]表示划分为1组的分组和的最大最小值，显然f[i][1] = sum(nums[0:i])，包含边界。
# 状态迁移方程：f[i][j] = min(max(f[k][j-1], sum(nums[k+1:]))), 1<= k < i
# 初值 f[0][0]=0
def splitArray(nums, m):
    n = len(nums)
    f = [[float("inf") for _ in range(m + 1)] for _ in range(n+1)]
    sub = [0]
    for elem in nums:
        sub.append(sub[-1] + elem)
    # sub[i]是前i个数的和

    f[0][0] = 0
    for i in range(1, n + 1):
        for j in range(1, min(i, m) + 1):
            for k in range(i):
                # k可以从0开始，因为float("inf")在max以及min之后，会被小的替换掉
                f[i][j] = min(f[i][j], max(f[k][j - 1], sub[i] - sub[k]))

    print(f)
    return f[n][m]