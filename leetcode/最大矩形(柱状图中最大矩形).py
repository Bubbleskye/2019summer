# 将问题转化到柱状图中的最大矩形
def maximalRectangle(matrix):
    if not matrix or len(matrix) == 0:
        return 0

    def largestRectangleArea(heights):
        stack = []
        res = 0
        heights = [0] + heights + [0]
        for i in range(len(heights)):
            while stack and heights[i] < stack[-1][0]:
                h, index = stack.pop()
                res = max(res, h * (i - stack[-1][1] - 1))
            stack.append([heights[i], i])
        return res

    row = len(matrix)
    col = len(matrix[0])
    res = 0
    # 获得以第i行为底的柱状图(连续的1)的高度
    for i in range(row):
        # rec中存储柱状图的高度
        rec = []
        for j in range(col):
            if matrix[i][j] == "1":
                k = i
                height = 0
                while k >= 0 and matrix[k][j] == "1":
                    height = height + 1
                    k = k - 1
                rec.append(height)
            else:
                rec.append(0)
        # print(rec)
        res = max(res, largestRectangleArea(rec))
    return res