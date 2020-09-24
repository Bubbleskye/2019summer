# 虽然是全排列 但不能用回溯法 会超时
# 找规律
# 如果 k≤(n−1)!，我们就可以确定排列的首个元素为 1；
# 如果 (n−1)!<k≤2⋅(n−1)!，我们就可以确定排列的首个元素为 2；
# 如果 (n-1) *(n-1)! < k ≤ n⋅(n−1)!，我们就可以确定排列的首个元素为 n。
# 因此第k个排列的首字母是ceil(k/(n-1)!)

def getPermutation(n, k):
    import math
    num = [str(i) for i in range(1, n+1)]
    res = ""
    behind=n-1
    while behind > -1:
        t = math.factorial(behind)
        # factorial整数的阶乘:n!=1×2×3×...×n
        # 0!=1
        # num中索引从0开始
        loc = math.ceil(k / t) - 1
        res = res+ num[loc]
        # 求出第k个排列的此时子序列首字母为num[loc]
        num.pop(loc)
        # 求出第k个排列在以num[loc]为开头的排列组合中的第几个(从1开始)
        k = k - loc*t
        # 又确定了一位，后缀个数-1
        behind=behind-1
    return res

print(getPermutation(2,2))

# 回溯
# def getPermutation(n, k):
#     output = []
#     nums = list(range(1, n + 1))
#
#     def backtrack(nums, res):
#         if len(res) == n:
#             output.append(int(res))
#             if len(output) == k:
#                 return True
#             else:
#                 return False
#         else:
#             for i in range(len(nums)):
#                 if backtrack(nums[0:i] + nums[i + 1:], res + str(nums[i])):
#                     return True
#
#     backtrack(nums, "")
#     return str(output[-1])