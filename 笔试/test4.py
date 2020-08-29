words="cloxy"
nums=list(range(0,len(words)))
m=3
output=[]
def backtrack(res,index):
    if index==len(words):
        if len(res)==m:
            output.append(res)
        return
    else:
        backtrack(res+[nums[index]],index+1)
        backtrack(res, index + 1)

backtrack([],0)
print(output)