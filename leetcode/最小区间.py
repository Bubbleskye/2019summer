# 该问题可以转化为，从 k 个列表中各取一个数，使得这 k 个数中的最大值与最小值的差最小。
# 假设这 kk 个数中的最小值是第 i 个列表中的 x，对于任意 j ！=i，设第 j 个列表中被选为 k 个数之一的数是 y，
# 则为了找到最小区间，y 应该取第 j 个列表中大于等于 x 的最小的数。
# 由于 k 个列表都是升序排列的，因此对每个列表维护一个指针
# 通过指针得到列表中的元素，指针右移之后指向的元素一定大于或等于之前的元素。
# 使用最小堆维护 k 个指针指向的元素中的最小值，同时维护堆中元素的最大值。
# 初始时，k 个指针都指向下标 0，最大元素即为所有列表的下标 0 位置的元素中的最大值。
# 每次从堆中取出最小值，根据最大值和最小值计算当前区间，如果当前区间小于最小区间则用当前区间更新最小区间
# 然后将对应列表的指针右移，将新元素加入堆中，并更新堆中元素的最大值。

# 对于tuple应用于heap来说，只能保证第一个元素是最小的，后面的元素从list的角度看不一定
def smallestRange(nums):
    import heapq
    heap = []
    n = len(nums)
    mi = float('inf')
    ma = float('-inf')
    # 初始化堆
    for i in range(n):
        # 堆中元组(值，第几个元素，第几个列表)
        heapq.heappush(heap, (nums[i][0], 0, i))
        # 第i个列表的第0个值
        mi = min(mi, nums[i][0])
        ma = max(ma, nums[i][0])

    res = [mi, ma]
    while True:
        small, smallindex, smalllist = heapq.heappop(heap)
        if smallindex == len(nums[smalllist]) - 1:
            # 列表中已经没有元素，break出
            break
        heapq.heappush(heap, (nums[smalllist][smallindex + 1], smallindex + 1, smalllist))
        ma = max(ma, nums[smalllist][smallindex + 1])
        mi = heap[0][0]
        # 最小堆的顶部元素heap[0]一定是最小的
        if ma - mi < res[1] - res[0]:
            res = [mi, ma]
        elif ma - mi == res[1] - res[0] and mi < res[0]:
            res = [mi, ma]
    return res

nums=[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
print(smallestRange(nums))