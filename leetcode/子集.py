def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    flag = 0
    for i in range(-1,-len(nums),-1):
        j = i - 1
        if nums[j] < nums[i]:
            nums[j], nums[i] = nums[i], nums[j]
            flag = 1
            break
        else:
            continue
    if flag == 1:
        return nums
    else:
        return nums.sort()

nums=[1,2,3]
nextPermutation(nums)
print(nums)
