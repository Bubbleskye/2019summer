def pattern132(nums):
    mod=100000007
    minnum={}
    minnum[0]=nums[0]
    for i in range(1,len(nums)):
        minnum[i]=max(minnum[i-1],nums[i])

    cnt=0
    stack=[]
    for j in range(-1,-len(nums)-1,-1):
        while stack and stack[-1]<=minnum[j]:
            stack.pop()
        if stack and nums[j]>stack[-1]:
            cnt=cnt+1
        stack.append(nums[j])


N=int(input())
nums=list(map(int, input().split()))
newnums=[]
for n in nums:
    newnums.append(abs(n))
if len(newnums)<3:
    print(0)
