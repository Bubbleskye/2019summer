# 用 dp[i][j] 表示 s 的前 i 个字符s[0:i]与 p 中的前 j 个字符p[0:j]是否能够匹配。
# 如果 p 的第 j 个字符是一个小写字母，那么我们必须在 s 中匹配一个相同的小写字母，即
# if s[i]=p[j] 则 dp[i][j]=dp[i-1][j-1]    elif p[j]=='.'则dp[i][j]=dp[i-1][j-1]  else: False
# 如果 p 的第 j 个字符是 *，* 跟着他前一个字符走，前一个能匹配上 s[i]，* 才能有用
# p[j-1] != s[i] : 重复0次 dp[i][j] = dp[i][j-2]
# p[j-1] == s[i] or p[j-1] == "."  即* 前面那个字符，能匹配 s[i]，或者 * 前面那个字符是万能的
# 重复1次 dp[i][j] = dp[i][j-1] 重复>=2次 dp[i][j] = dp[i-1][j]
# p[j] == s[i]:dp[i][j] = dp[i-1][j-1]
# p[j] == ".":dp[i][j] = dp[i-1][j-1]
# p[j] =="*":
# 3.1 p[j-1] != s[i]:dp[i][j] = dp[i][j-2]
# 3.2 p[i-1] == s[i] or p[j-1] == ".":
# dp[i][j] = dp[i-1][j] // 多个字符匹配的情况  or dp[i][j] = dp[i][j-1] // 单个字符匹配的情况  or dp[i][j] = dp[i][j-2] // 没有匹配的情况
# https://leetcode-cn.com/problems/regular-expression-matching/solution/shou-hui-tu-jie-wo-tai-nan-liao-by-hyj8/
# 从右向左考虑 思考dp表达式

def isMatch(s, p) :
    s_len = len(s)
    p_len = len(p)
    dp = [[False for _ in range(p_len + 1)] for _ in range(s_len + 1)]
    # print(dp)
    dp[0][0] = True
    # s是空字符
    for i in range(p_len):
        if p[i] == "*" and dp[0][i - 1]:
            # dp[0][i-1]是前两个字母的情况
            dp[0][i + 1] = True
    # print(dp)
    for i in range(s_len):
        for j in range(p_len):
            if p[j] == s[i] or p[j] == ".":
                dp[i + 1][j + 1] = dp[i][j]
            elif p[j] == "*":
                if p[j - 1] != s[i]:
                    dp[i + 1][j + 1] = dp[i + 1][j - 1]
                if p[j - 1] == s[i] or p[j - 1] == ".":
                    dp[i + 1][j + 1] = (dp[i][j + 1] or dp[i + 1][j] or dp[i + 1][j - 1])
    # print(dp)
    return dp[-1][-1]