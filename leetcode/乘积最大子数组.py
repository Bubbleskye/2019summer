def maxProduct(nums) :
# 因为正负号有反转,所有最大最小都储存下来
# 以当前节点为终结节点的最大连续子序列乘积imax[i]=max(imax[i-1]*nums[i],nums[i],imin[i-1]*nums[i])
# 以当前节点为终结节点的最小连续子序列乘积imin[i]=min(imax[i-1]*nums[i],nums[i],imin[i-1]*nums[i])
# 如果nums[i]==0,则从i+1重新开始计算
    imax=[False for _ in range(len(nums))]
    imin=[False for _ in range(len(nums))]
    imax[0]=nums[0]
    imin[0]=nums[0]
    for i in range(len(nums)):
        imax[i]=max(imax[i-1]*nums[i],nums[i],imin[i-1]*nums[i])
        imin[i]=min(imax[i-1]*nums[i],nums[i],imin[i-1]*nums[i])
    return max(max(imax), max(imin))

nums=[2,0,-1]
print(maxProduct(nums))