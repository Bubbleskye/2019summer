height=[0,1,0,2,1,0,1,3,2,1,2,1]
# 真正难点在于: 在一个位置能容下的雨水量等于它左右两边柱子最大高度的最小值减去它的高度
# 问题就变成了：如何找所有位置的左右两边的柱子的最大值
# 一列一列算每个上面有多少水
# 双指针
if not height:
    print(0)
left = 0
right = len(height) - 1
max_left = height[left]
max_right = height[right]
ans = 0
while left < right:
    if max_left <= max_right:
        # 当左边最大值,小于右边最大值,此时,左边列上面的水可以确定,因为右边一定有列可以兜住
        ans =ans+ max_left - height[left]
        left =left+ 1
        max_left = max(height[left], max_left)

    if max_left > max_right:
        ans =ans+ max_right - height[right]
        right =right- 1
        max_right = max(height[right], max_right)
print(ans)

