# 用 dp[i][j] 表示 s 的前 i 个字符s[0:i]与 p 中的前 j 个字符p[0:j]是否能够匹配
# 如果 p 的第 j 个字符是一个小写字母，那么我们必须在 s 中匹配一个相同的小写字母，即
# if s[i]==p[j] 或 p[j]=='.' 则 dp[i+1][j+1]=dp[i][j]  else: False
# 如果 p 的第 j 个字符是 *，* 跟着他前一个字符走，前一个能匹配上 s[i]，* 才能有用
# p[j-1] != s[i] : *代表消失 看p[j-2]为止能否与s匹配上，dp[i + 1][j + 1] = dp[i + 1][j - 1]
# p[j-1] == s[i] or p[j-1] == "."  即* 前面那个字符，能匹配 s[i]，或者 * 前面那个字符是万能的
# 此时*可以让p[j-1]消失/出现1次/出现>=2次
# 消失,还是看p[j-2]能否匹配上s[i] dp[i + 1][j + 1] = dp[i + 1][j - 1]
# 出现1次,看p[j-1]匹配s[i]的结果,dp[i+1][j+1] = dp[i+1][j]
# 重复>=2次,即a*代表多个a,我们只用拿出1个a与s[i]抵消,dp[i+1][j+1] = dp[i][j+1]
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
        if p[i] == "*" and dp[0][i-1]:
            # 若p[i] 是 '*',说明第 i-1,i 位可有可无
            # 那么如果前 i - 2 个已经匹配上，前 i 个也可以匹配上
            dp[0][i + 1] = True
    # print(dp)
    for i in range(s_len):
        for j in range(p_len):
            if p[j] == s[i] or p[j] == ".":
                dp[i + 1][j + 1] = dp[i][j]
            elif p[j] == "*":
                if p[j - 1] != s[i]:
                    # *代表p[j-1]出现0次
                    dp[i + 1][j + 1] = dp[i + 1][j - 1]
                if p[j - 1] == s[i] or p[j - 1] == ".":
                    dp[i + 1][j + 1] = (dp[i][j + 1] or dp[i + 1][j] or dp[i + 1][j - 1])
    # print(dp)
    return dp[-1][-1]