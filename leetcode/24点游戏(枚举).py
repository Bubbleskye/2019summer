# 只有 4 张牌，且只能执行 4 种操作。具体来说，我们有 12 种方式先选出两个数字（有序），并执行 4 种操作之一（12 * 4）。
# 然后，剩下 3 个数字，我们从中选择 2 个并执行 4 种操作之一（6 * 4）。
# 最后我们剩下两个数字，并在 2 * 4 种可能之中作出最终选择。
# 最多也只有 (12 * 4) * (6 * 4) * (2 * 4) = 9216 种可能性，这使得我们可以尝试所有这些可能。
def judgePoint24(nums):
    if not nums:
        return False

    def helper(nums):
        if len(nums) == 1:
            print(nums[0])
            return abs(nums[0] - 24) < 1e-6
        #     计算出结果不一定为整24
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    # 找出除了nums[i]和nums[j]之外的num
                    newnums=[nums[k] for k in range(len(nums)) if k!=i and k!=j]
                    if helper(newnums + [nums[i] + nums[j]]):
                        return True
                    if helper(newnums + [nums[i] - nums[j]]):
                        return True
                    if helper(newnums + [nums[i] * nums[j]]):
                        return True
                    if nums[j] != 0 and helper(newnums + [nums[i] / nums[j]]):
                        return True
        return False

    return helper(nums)

nums=[3,3,8,8]
print(judgePoint24(nums))