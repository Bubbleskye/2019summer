def longestMountain(A):
    res = 0
    i = 0
    while i < len(A):
        j = i
        # 跳出循环时，找到上升的终点，即山顶
        while j + 1 < len(A) and A[j] < A[j + 1]:
            j = j + 1
        mid = j
        # 跳出循环时，找到下降的终点
        while j + 1 < len(A) and A[j] > A[j + 1]:
            j = j + 1
        # 判断是否构成山脉
        if i < mid < j:
            res = max(res, j - i + 1)
        # 如果未构成山脉，有两种可能：只有下降段/没有移动过
        # 如果是平山，i后移一位，否则下降的终点作为新的起点
        if i == j:
            i = i + 1
        else:
            i = j
    return res


def longestMountain1(A):
    res=0
    start=0
    end=0
    while start < len(A):
        j=start
        while j+1<len(A) and A[j+1]>A[j]:
            j=j+1
        mid=j
        while j+1<len(A) and A[j+1]<A[j]:
            j=j+1
        end=j
        if start<mid<end:
            res=max(res,end-start+1)
            start = end
        else:
            if start==end:
                start=end+1
            else:
                start=end
    return res
A=[2,1,4,7,3,2,5]
print(longestMountain1(A))