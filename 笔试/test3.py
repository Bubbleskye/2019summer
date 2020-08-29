P=int(input())
N=int(input())

def findpossible(words,m):
    nums = list(range(0, len(words)))
    output=[]
    def backtrack(res,index):
        if index==len(words):
            if len(res)==m:
                output.append(res)
            return
        else:
            backtrack(res+[nums[index]],index+1)
            backtrack(res, index + 1)
    backtrack([], 0)



for _ in range(N):
    word,m,n=input.strip().split()
