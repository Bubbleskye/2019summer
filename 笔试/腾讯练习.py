# 给定一个字符串s，你可以从中删除一些字符，使得剩下的串是一个回文串。如何删除才能使得回文串最长呢？
# 输出需要删除的字符个数。
# 输入例子1:
# abcda
# google
# 输出例子1:
# 2
# 2
def hw(nums):
    dp=[[1 for _ in range(len(nums))] for _ in range(len(nums))]
    for j in range(len(nums)):
        for i in range(0,j+1):
            if j-i==0:
                dp[i][j]=1
            elif j-i==1 and nums[j]==nums[i]:
                dp[i][j]=2
            elif nums[i]==nums[j]:
                dp[i][j]=dp[i+1][j-1]+2
            else:
                dp[i][j]=max(dp[i+1][j-1],dp[i+1][j],dp[i][j-1])
    return dp[0][-1]

# 一组数据有多行，但每一行是一个单独的测试
# 的读入方法
if __name__ == "__main__":
    import sys
    while True:
        s = sys.stdin.readline().strip()
        if not s:
            break
        if len(s)==0 or len(s)==1:
            print(0)
        else:
            maxlen=hw(s)
            print(len(s)-maxlen)

