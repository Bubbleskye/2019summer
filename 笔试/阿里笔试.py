class Solution:
    def __init__(self):
        self.count=0
    def backtrack(self,res,nums):
        self.count=self.count+len(res)
        for i in range(len(nums)):
            self.backtrack(res + [nums[i]], nums[i + 1:])
        return
n = int(input())
people = list(range(1, n + 1))
solution=Solution()
for i in range(len(people)):
    solution.backtrack([people[i]], people[i + 1:])
print(solution.count)

# 用于需要__init__设置全局变量的情况
