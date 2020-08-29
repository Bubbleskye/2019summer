def rob(nums):
    l = len(nums)
    if l == 0:
        return 0
    if l == 1:
        return nums[0]
    if l == 2:
        return max(nums)
    tmp = len(nums) // 2
    sum1 = rob(nums[0:tmp]) + rob(nums[tmp + 1:l])
    sum2 = rob(nums[0:tmp + 1]) + rob(nums[tmp + 2:l])
    return max(sum1, sum2)

nums=[2,7,9,3,1]
print(rob(nums))