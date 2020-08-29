def maxSubArray(nums) :
    n = len(nums)
    # 递归终止条件
    if n == 1:
        return nums[0]
    else:
        # 递归计算左半边最大子序和
        max_left = maxSubArray(nums[0:len(nums) // 2])
        # 递归计算右半边最大子序和
        max_right = maxSubArray(nums[len(nums) // 2:len(nums)])

    # 计算中间的最大子序和，从右到左计算左边的最大子序和，从左到右计算右边的最大子序和，再相加
    max_l = nums[len(nums) // 2 - 1]
    tmp = 0
    for i in range(len(nums) // 2 - 1, -1, -1):
        tmp = tmp + nums[i]
        #           tmp记录累加和
        max_l = max(tmp, max_l)
    max_r = nums[len(nums) // 2]
    tmp = 0
    for i in range(len(nums) // 2, len(nums)):
        tmp += nums[i]
        max_r = max(tmp, max_r)
    # 返回三个中的最大值
    return max(max_right, max_left, max_l + max_r)

nums=[-2,1,-3,4,-1,2,1,-5,4]
A=maxSubArray(nums)
print(A)

# 这里采用递归的算法.没有用动态规划
# 而是用了分治算法,区别在于分治算法中没有重叠的子子问题


#动态规划
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