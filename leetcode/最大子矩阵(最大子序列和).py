def getMaxMatrix(self, matrix):
    row = len(matrix)
    col = len(matrix[0])
    maxArea = float('-inf')  # 最大面积
    res = [0, 0, 0, 0]

    # 按列合并，计算前缀和
    for left in range(col):  # 从左到右，从上到下，滚动遍历
        colSum = [0 for _ in range(row)]
        # 以left为左边界，每行的总和，相当于有一个转置
        for right in range(left, col):  # 这一列每一位为右边界
            for i in range(row):  # 遍历列中每一位，计算前缀和
                colSum[i] = colSum[i] + matrix[i][right]

            startX, endX, maxAreaCur = self.getMax(colSum)  # 在left，right为边界下的矩阵中，前缀和colSum的最大值
            if maxAreaCur > maxArea:
                res = [startX, left, endX, right]  # left是起点y轴坐标，right是终点y轴坐标
                maxArea = maxAreaCur
    return res


# 这一列中，找最大值，同时记录起点，终点
# 因为传进来的是列的前缀和，所以返回的起点、终点代表的是行坐标
def getMax(self, nums):
    n = len(nums)
    # dp存储的是到第i个数字位置的最大子序列和
    dp = [0 for _ in range(len(nums))]
    dp[0] = nums[0]
    # head存储的是到第i个位置位置的最大子序和的起点的坐标
    head = [0 for _ in range(len(nums))]
    for i in range(1, n):
        if dp[i - 1] + nums[i] > nums[i]:
            dp[i] = dp[i - 1] + nums[i]
            head[i] = head[i - 1]
        else:
            dp[i] = nums[i]
            head[i] = i
    maxVal = max(dp)
    maxindex = dp.index(maxVal)
    start = head[maxindex]
    end = maxindex
    return start, end, maxVal  # 起点，终点，最大前缀和（最大面积）

matrix=[[9,-8,1,3,-2],[-3,7,6,-2,4],[6,-4,-4,8,-7]]
print(getMaxMatrix(matrix))