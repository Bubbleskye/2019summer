def combinationSum(candidates,target) :
    output = []

    def backtrack(sum, target, candidates, res):
        if sum < target:
            for i in range(len(candidates)):
                if sum + candidates[i] >target:
                    return
                if sum+candidates[i]==target:
                    tmp=res + [candidates[i]]
                    tmp.sort()
                    if tmp not in output:
                        output.append(res + [candidates[i]])
                    break
                backtrack(sum + candidates[i], target, candidates, res + [candidates[i]])
        return output

    backtrack(0, target, candidates, [])
    return output

candidates = [2,3,5]
target = 8
candidates.sort()
output=combinationSum(candidates,target)
print(output)