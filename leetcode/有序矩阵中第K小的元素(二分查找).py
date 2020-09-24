# 给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第k小的元素。
# 请注意，它是排序后的第k小元素，而不是第k个元素。（即相同的元素代表着不同的k）
#
# 示例:
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
# 返回 13

def kthSmallest(matrix, k):
    row = len(matrix)
    col = len(matrix[0])
    left = matrix[0][0]
    # 左上角——最小
    right = matrix[row - 1][col - 1]
    # 右下角——最大

    def count(row, col, matrix, value):
        # 计算小于等于value的数有多少个
        i = 0
        j = col - 1
        ans = 0
        # 从右上角开始搜索
        while i < row and j >= 0:
            if matrix[i][j] <= value:
                # 去掉一行
                ans = ans + j + 1
                i = i + 1
            else:
                # 去掉一列
                j = j - 1
        return ans

    # 第k小的意思是至少有k个小于等于本身的数（可能大于k，这个数有多个相同的）
    # <=第k小的元素数量 >=k
    while left<right:
        mid = left + (right - left) // 2
        cnt = count(row, col, matrix, mid)
        # 如果cnt小于k，说明我们选择的值太小了，肯定不符合条件，我们需要调整左区间为mid + 1
        if cnt < k:
            left = mid + 1
        # 如果cnt>=k,说明我们选择的中间值正好或者偏大
        else:
            right=mid
    return left
# 相等的时候一定在matrix里面。 因为原问题一定有解，找下界使得start不断的逼近于真实的元素.
matrix=[[1,2,4],[2,3,4]]
k=4
print(kthSmallest(matrix, k))