# 将结果分为两种可能的情况，一种是不跨边界的情况直接求解
# 一种是跨边界则将问题转化为求解不跨边界的子数组和最小
# 解释：「中间部分」最小，等价于「两头最大」。「两头最大」等价于「两个相同数组交接部分的区域和最大」。
# 此种方法需要考虑数组中元素全为负数的情况

def maxSubarraySumCircular(A):
    # bigdp[i]以i为末尾的最大子数组和
    bigdp = [0 for _ in range(len(A))]
    bigdp[0] = A[0]
    # smalldp[i]以i为末尾的最小子数组和
    smalldp = [0 for _ in range(len(A))]
    smalldp[0] = A[0]
    find = False
    for i in range(1, len(A)):
        if A[i] >= 0:
            find = True
        if bigdp[i - 1] + A[i] > A[i]:
            bigdp[i] = bigdp[i - 1] + A[i]
        else:
            bigdp[i] = A[i]
        if smalldp[i - 1] + A[i] < A[i]:
            smalldp[i] = smalldp[i - 1] + A[i]
        else:
            smalldp[i] = A[i]

    if find:
        return max(max(bigdp), sum(A) - min(smalldp))
    else:
        # 如果数组全为负
        return max(A)