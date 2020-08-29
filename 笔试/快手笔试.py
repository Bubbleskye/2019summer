def generator(nums):
    s=nums[0]
    a=nums[1]
    b=nums[2]
    p=nums[3]
    res=[]
    dict={}
    res.append(s)
    dict[s]=1
    i=1
    while True:
        tmp=(res[i-1]*a+b)%p
        if tmp not in dict:
            dict[tmp]=1
        else:
            if dict[tmp]==2:
                break
            else:
                dict[tmp]=dict[tmp]+1
        res.append(tmp)
        i=i+1
    return res

def longestCommonSubsequence(text1,text2):
    if not text1 or not text2:
        return 0
    dp = [[0 for _ in range(len(text1) + 1)] for _ in range(len(text2) + 1)]
    for i in range(len(text2)):
        for j in range(len(text1)):
            if text2[i] == text1[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    return dp[-1][-1]

# nums=[4,2,1,6]
# print(generator(nums))

# 输入时有n组，每组2行
# 每行都是数字
if __name__ == "__main__":
    n = int(input())
    mx = []
    str=[]
    for i in range(n*2):
        m = list(map(int, input().split()))
        mx.append(m)
        str.append(generator(m))
    j=0
    while j < len(mx):
        if mx[j]==mx[j+1]:
            print(len(str[j]))
        else:
            print(longestCommonSubsequence(str[j],str[j+1]))
        j=j+2
