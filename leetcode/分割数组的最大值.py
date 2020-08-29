# 状态定义：f[i][j]表示nums[0] ~ nums[i]共i+1个元素划分为j组的和的最大的最小值。
# 可初始化的状态：f[i][1]表示nums[0]~nums[i]划分为1组的分组和的最大最小值，显然f[i][1] = sum(nums[0:i+1])，包含边界。
# 状态迁移方程：f[i][j] = min(max(f[k][j-1], sum(nums[k+1:]))), 0<= k < i
# 最后一个段不确定，前面有i-1段
def splitArray(nums, m):
    n = len(nums)
    f = [[float("inf") for _ in range(m + 1)] for _ in range(n + 1)]
    sub = [0]
    for elem in nums:
        sub.append(sub[-1] + elem)
        # sub[i]是sum(nums[0:i+1])即0~i的和

    f[0][0] = 0
    for i in range(1, n + 1):
        for j in range(1, min(i, m) + 1):
            for k in range(i):
                f[i][j] = min(f[i][j], max(f[k][j - 1], sub[i] - sub[k]))
    print(f)
    return f[n][m]