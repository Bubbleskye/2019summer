# 给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第k小的元素。
# 请注意，它是排序后的第k小元素，而不是第k个元素。
#
# 示例:
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
# 返回 13。
def kthSmallest(matrix, k):
    row = len(matrix)
    col = len(matrix[0])
    left = matrix[0][0]
    right = matrix[row - 1][col - 1]

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
    # 第k小的意思是有k个小于等于他的数
    while left<right:
        mid = left + (right - left) // 2
        cnt = count(row, col, matrix, mid)
        # 如果count小于k，说明我们选择的值太小了，肯定不符合条件，我们需要调整左区间为mid + 1
        if cnt < k:
            left = mid + 1
        # 如果count等于k-1，说明我们选择的中间值正好 或者
        # （我们要找的是一个在矩阵中的数）偏大（这里的意思时，这个中间值不在矩阵中，但略小一点的在，那小于等于略小一点的数的个数也有k个
        # 略大一点的数不是一定满足，比如略大一点的数在矩阵中，那小于等于它的一定大于k
        # 所以往下找 right=mid-1
        elif cnt==k:
            right=mid
        # 如果count大于k 说明此时的值太大了 或者
        # 正好（这个正好的值有多个 因为在count中相等的值计数到了小于的数量中）
        # 因此这里不能调整为mid - 1， 否则可能会得不到结果
        else:
            right=mid
    return left
# 相等的时候一定在matrix里面。 因为原问题一定有解，找下界使得start不断的逼近于真实的元素.
matrix=[[1,2],[1,3]]
k=3
print(kthSmallest(matrix, k))