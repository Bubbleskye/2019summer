def canDivideIntoSubsequences(nums, K):
    if not nums or len(nums) < K:
        return False
    maxnum = 0
    dict = {}
    for i in range(len(nums)):
        if nums[i] not in dict:
            dict[nums[i]] = 1
        else:
            dict[nums[i]] = dict[nums[i]] + 1
    for key, value in dict.items():
        maxnum = max(maxnum, value)
    if maxnum * K <= len(nums):
        return True
    else:
        return False

# 类似于任务调度器
# 先把有最多的相同的数的数量统计出来，其他的数要不放在他前面，要不放在他后面，都不会影响总的序列个数
# 所以只要看nums的个数是否满足<=最多的相同的数的数量*k