def minNumber(nums):
    # 新的排序规则：如果m和n两个数字，mn<nm，则m排在n前面
    # 考虑大数问题，mn与nm一定是位数相同的字符，所以不用按数字比较大小，按字符串比较大小即可
    # 字符串比较大小，比的是ascii码，对于数字来说ASCII码从0-9递增
    def quickSort(nums, left, right):
        if left >= right:
            return nums

        low = left
        high = right
        key = nums[low]

        while left < right:
            while left < right and str(nums[right]) + str(key) > str(key) + str(nums[right]):
                right = right - 1
            nums[left] = nums[right]
            while left < right and str(nums[left]) + str(key) <= str(key) + str(nums[left]):
                left = left + 1
            nums[right] = nums[left]

        nums[left] = key

        quickSort(nums, low, left - 1)
        quickSort(nums, left + 1, high)

    quickSort(nums, 0, len(nums) - 1)
    res=""
    for n in nums:
        res=res+str(n)
    return res

nums=[10,2]
print(minNumber(nums))