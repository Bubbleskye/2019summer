def quickSort(nums, left, right):
    if left >= right:
        return nums

    low = left
    high = right
    key = nums[low]

    while left < right:
        while left < right and nums[right] > key:
            right = right - 1
        nums[left] = nums[right]
        while left < right and nums[left] <= key:
            left =left + 1
        nums[right] = nums[left]

    nums[left] = key

    quickSort(nums, low, left - 1)
    quickSort(nums, left + 1, high)
    return nums

nums=[5,1,1,2,0,0]
result=quickSort(nums, 0, len(nums)-1)
print(result)
