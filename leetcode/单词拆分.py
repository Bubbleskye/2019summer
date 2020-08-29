# 回溯__超时
# s="abcd"
# wordDict=["a","abc","b","cd"]
# def backtrack(res,wordDict):
#     if len(res)==0:
#         return True
#     flag=False
#     for i in range(len(res)):
#         if res[:i + 1] in wordDict:
#             flag = backtrack(res[i + 1:], wordDict)
#         if flag:
#             return flag
# print(backtrack(s,wordDict))

# 动态规划+双指针
# dp[i]表示从头到i这(i+1)个字符串有没有在字典中组合出现
s="abcd"
wordDict=["a","abc","b","cd"]
dp=[False for _ in range(len(s)+1)]
dp[0]=True
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        if(dp[i] and (s[i:j] in wordDict)):
            dp[j]=True
print(dp[-1])

