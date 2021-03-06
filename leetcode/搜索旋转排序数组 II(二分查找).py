def search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        # print(left, right)
        mid = left + (right - left) // 2
        # 等于目标值
        if nums[mid] == target:
            return True
        # 处理相同元素
        if nums[mid] == nums[left] == nums[right]:
            left += 1
            right -= 1

        # 前部分是有序的，可以利用二分查找
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # 后半部分是有序的，可以利用二分查找
        elif nums[right]>=nums[mid]:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return False

nums = [2,5,6,1,1,1,2]
target = 2
search(nums, target)