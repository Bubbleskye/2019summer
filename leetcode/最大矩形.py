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
    for i in range(row):
        rec = []
        for j in range(col):
            if matrix[i][j] == "1":
                k = i
                s = 0
                while k >= 0 and matrix[k][j] == "1":
                    s = s + int(matrix[k][j])
                    k = k - 1
                rec.append(s)
            else:
                rec.append(0)
        # print(rec)
        res = max(res, largestRectangleArea(rec))
    return res