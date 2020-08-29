def canDivideIntoSubsequences(nums, K):
    if not nums or len(nums) < K:
        return False
    from collections import Counter
    numsdict = Counter(n for n in nums)
    v = numsdict.values()
    if max(v) * K > len(nums):
        return False
    return True

# 类似于任务调度器