# 首先，要想找到第 i 位置最大面积是什么？
# 是以i 为中心，向左找第一个小于 heights[i] 的位置 left_i；向右找第一个小于于 heights[i] 的位置 right_i，
# 即最大面积为 heights[i] * (right_i - left_i -1)

# 栈中存储的索引值
# 我们找的是元素左右最近的比它小的元素的位置
# 找到后会弹出栈顶元素，循环弹出直到栈顶值小于目前要加入的值，所以栈是一个递增的栈

def largestRectangleArea(heights):
    stack = []
    heights = [0] + heights + [0]
    res = 0
    for i in range(len(heights)):
        # print(stack)
        while stack and heights[i]<heights[stack[-1]]:
            tmp = stack.pop()
            res = max(res, (i - stack[-1] -1) * heights[tmp])
        stack.append(i)
    return res
heights=[2,1,5,6,2,3]
print(largestRectangleArea(heights))