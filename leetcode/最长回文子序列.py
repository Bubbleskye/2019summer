# dp[i][j]表示i到j之间的最长回文子序列
# 当i到j不是连续的回文子串时，dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
def longestPalindromeSubseq(s):
    dp = [[1 for _ in range(len(s))] for _ in range(len(s))]
    for j in range(len(s)):
        for i in range(j, -1, -1):
            if j - i == 0:
                dp[i][j] = 1
            elif j - i == 1 and s[j] == s[i]:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][-1]
# 因为涉及到dp[i + 1][j]，所以i应该倒着来