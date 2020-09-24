def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    i = 0
    cnt = 0
    while i < len(nums) - cnt:
        if nums[i] != 0:
            i = i + 1
        else:
            j = i + 1
            while j < len(nums) - cnt:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
                j = j + 1
            cnt = cnt + 1

nums=[0,0,1]
print(moveZeroes(nums))