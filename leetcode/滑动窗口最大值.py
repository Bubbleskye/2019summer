def maxSlidingWindow(nums, k):
    if not nums:
        return 0
    if len(nums) <= k:
        return [max(nums)]
    from collections import deque
    deque = deque()
    # 建立双端队列 存储最大值的索引 索引0为最大值的索引
    res = []
    for i in range(len(nums)):
        while deque and deque[0] < i - k + 1:
            deque.popleft()
            # 如果目前的最大值的索引已经不在当前滑窗内，则从左边弹出
        while deque and nums[i] > nums[deque[-1]]:
            deque.pop()
            # 如果目前的值比当前队列末尾值大，则将小于这个值的值全部从右边弹出，因为一旦滑窗中有这个元素，前面比它小的值都没用
        deque.append(i)
        if i >= k - 1:
            res.append(nums[deque[0]])
    #         从第k-1个值开始加入
    return res