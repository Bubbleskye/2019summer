def countSmaller(nums):
    if not nums:
        return []
    n = len(nums)
    sort = [nums[-1]]
    dp = [0 for i in range(n)]
    dp[-1] = 0
    for i in range(n - 2, -1, -1):
        index = binarySearch(nums[i], sort)
        dp[i] = index
        sort.insert(index, nums[i])
    return dp

# 用二分查找找到应该插入的位置
def binarySearch(a, sort):
    n = len(sort)
    left = 0
    right = n - 1
    while left < right:
        mid = (left + right) // 2
        if sort[mid] >= a:
            right = mid
        elif sort[mid] < a:
            left = mid + 1
    if sort[left] < a:
        return left + 1
    else:
        return left