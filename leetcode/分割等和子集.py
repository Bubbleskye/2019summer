nums=[1,2,5]
if sum(nums)%2!=0:
    print(False)
else:
    half= int(sum(nums)/2)
# dp[i][h]=dp[i-1][h] or dp[i-1][h-nums[i]]
# 从尾部开始考虑 在到i时，可以达到和为h的两种可能1、前面就达到了 2、加上第i个正好达到
# dp[i][h]表示从数组的 [0, i] 这个子区间内挑选一些正整数，每个数只能用一次，使得这些数的和恰好等于 h。
dp=[[False for _ in range(half+1)] for _ in range(len(nums))]
for i in range(len(nums)):
    if nums[i]<=half:
        dp[i][nums[i]]=True
for i in range(1,len(nums)):
    for h in range(half+1):
        dp[i][h]= dp[i-1][h] or dp[i-1][h-nums[i]]
print(dp[len(nums)-1][half])