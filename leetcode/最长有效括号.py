# 我们用 dp[i] 表示以 i 结尾的最长有效括号；
# 当 s[i] 为 (,dp[i] 必然等于 0，因为不可能组成有效的括号；
# 那么 s[i] 为 )
# 2.1 当 s[i-1] 为 (，那么 dp[i] = dp[i-2] + 2；
# 2.2 当 s[i-1] 为 ) 并且 s[i-dp[i-1] - 1] 为 (，那么 dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]；

def longestValidParentheses(s):
    if len(s) == 0:
        return 0
    dp = [0 for _ in range(len(s))]
    res = 0
    for i in range(len(s)):
        if i > 0 and s[i] == ")":
            if s[i - 1] == "(":
                dp[i] = dp[i - 2] + 2
            elif s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
    return max(dp)

s="()(())"
print(longestValidParentheses(s))