def numDecodings(s):
    # 主要是对于0的处理方法
    if not s:
        return 0
    if s[0] == "0":
        return 0
    if len(s) == 1:
        return 1
    dp = [0 for _ in range(len(s))]
    dp[0] = 1
    if 10 <= int(s[0] + s[1]) <= 26 and s[1] != "0":
        dp[1] = 2
    elif s[1] == "0" and int(s[0] + s[1]) > 26:
        return 0
    else:
        dp[1] = 1
    for i in range(2, len(s)):
        if s[i] == "0" and 10 <= int(s[i - 1] + s[i]) <= 26:
            dp[i] = dp[i - 2]
        elif s[i] == "0":
            return 0
        elif 10 <= int(s[i - 1] + s[i]) <= 26:
            dp[i] = dp[i - 1] + dp[i - 2]
        else:
            dp[i] = dp[i - 1]
    return dp[-1]

s="12120"
print(numDecodings(s))