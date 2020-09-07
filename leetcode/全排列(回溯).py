def permute(nums):
    output = []
    n = len(nums)

    def backtrack(res, nums):
        if len(res) == n and res not in output:
            output.append(res)
            return
        else:
            for i in range(len(nums)):
                backtrack(res + [nums[i]], nums[0:i] + nums[i + 1:])

    backtrack([], nums)
    return output

nums=[1,2,3]
output=permute(nums)
print(output)