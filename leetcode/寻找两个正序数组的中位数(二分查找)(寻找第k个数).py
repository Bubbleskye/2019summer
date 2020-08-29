# 时间复杂度 O(log(m + n)) —— log即二分查找
def findMedianSortedArrays(nums1, nums2):
    def helper(nums1, nums2, k):
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1  # 保持nums1比较长
        if len(nums2) == 0:
            return nums1[k - 1]  # 短数组空，直接返回
        if k == 1:
            return min(nums1[0], nums2[0])  # 找最小数，比较数组首位
        t = min(k//2,len(nums2))
        # 如果nums1[k/2]>=nums2[k/2]，这意味着：nums2数组的左半边都不需要考虑了，因为肯定会比第k小的数要来得小。
        if nums1[t - 1] >= nums2[t - 1]:
            return helper(nums1, nums2[t:], k - t)
        # else,这意味着：nums1数组的左半边都不需要考虑了，因为肯定会比第k小的数要来得小。
        else:
            return helper(nums1[t:], nums2, k - t)


    n=len(nums1)
    m=len(nums2)
    if (n + m) % 2 == 0:
        left = (n + m) // 2
        right = (n + m) // 2 + 1
    else:
        left = (n + m) // 2 + 1
        right = left
    return (helper(nums1,nums2,left) + helper(nums1,nums2,right)) * 0.5


nums1=[1]
nums2=[2,3,4,5]
print(findMedianSortedArrays(nums1, nums2))