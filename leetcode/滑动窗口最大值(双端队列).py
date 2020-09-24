# 双端队列第一个值是此时滑动窗口中的最大值
# 相当于我们此时的i是滑动窗口中的最后一个值,在这个值进入队列前,首先将已经不在滑动窗口中的值popleft出去
# 再将小于这个数,且索引在这个数前面的值也pop出去
# 最后,由于队列是递减的,所以,对首的即是最大值

def maxSlidingWindow(nums, k):
    if not nums:
        return 0
    if len(nums) <= k:
        return [max(nums)]
    from collections import deque
    deque = deque()
    # 建立双端队列 存储索引 索引0为最大值的索引
    # 队列中始终保持递减
    res = []
    for i in range(len(nums)):
        while deque and deque[0] < i - k + 1:
            # 如果目前的最大值的索引已经不在当前滑窗内，则从左边弹出
            deque.popleft()

        while deque and nums[i] > nums[deque[-1]]:
            # 如果目前的值比当前队列末尾值大，则将小于这个值的值全部从右边弹出
            # 因为一旦滑窗中有这个元素，前面比它小的值都没用
            deque.pop()

        deque.append(i)
        if i >= k - 1:
            res.append(nums[deque[0]])
    #         从第k-1个值开始加入
    return res

nums = [1,3,-1,-3,5,3,6,7]
k=3
print(maxSlidingWindow(nums, k))