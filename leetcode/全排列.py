def permute(nums):
    output = []

    def backtrack(res, nums):
        for i in range(len(nums)):
            if len(nums) == 1:
                output.append(res+[nums[i]])
                return output
            backtrack(res + [nums[i]], nums[0:i]+nums[i+1:])

    backtrack([], nums)
    return output

nums=[1,2,3]
output=permute(nums)
print(output)