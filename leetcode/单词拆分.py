# 回溯__超时
# s="abcd"
# wordDict=["a","abc","b","cd"]
# def backtrack(res):
#     if len(res)==0:
#         return True
#     for i in range(len(res)):
#         if res[:i + 1] in wordDict:
#             if backtrack(res[i + 1:]):
#                   return True
# print(backtrack(s))

# 动态规划
# dp[i]表示前i个字符串（到s[i-1]为止）有没有在字典中组合出现
# 一共有前n个字符
# 初值dp[0]=True
# dp[i]=dp[j] and s[j:i] in wordDict
s="abcd"
wordDict=["a","abc","b","cd"]
dp=[False for _ in range(len(s)+1)]
dp[0]=True
for i in range(1,len(s)+1):
    for j in range(i):
        if dp[j] and s[j:i] in wordDict:
            dp[i]=True
print(dp[-1])

