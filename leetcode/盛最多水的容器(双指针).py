# 双指针
# 水量等于长的最小值*宽
# 随着从两边向内缩，长肯定是越来越小的，所以我们要去找宽变大的方向
def maxArea(height):
    left = 0
    right = len(height) - 1
    Area = 0
    while left < right:
        Area = max(Area, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left = left + 1
        else:
            right = right - 1
    return Area