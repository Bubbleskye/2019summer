def subsets(nums):
    output = []
    n = len(nums)

    def backtrack(index, res):
        if index == n:
            if res not in output:
                output.append(res)
            return
        else:
            backtrack(index + 1, res + [nums[index]])
            backtrack(index + 1, res)

    backtrack(0, [])
    return output