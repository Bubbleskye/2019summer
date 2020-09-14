def combinationSum(candidates,target) :
    output = []

    def backtrack(nums, res):
        if sum(res) == target:
            res.sort()
            if res not in output:
                output.append(res)
            return
        else:
            for i in range(len(nums)):
                if sum(res) + nums[i] <= target:
                    backtrack(nums, res + [nums[i]])
                else:
                    return

    backtrack(candidates, [])
    return output

candidates = [2,3,5]
target = 8
candidates.sort()
output=combinationSum(candidates,target)
print(output)