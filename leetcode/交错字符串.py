def isInterleave(s1, s2, s3):
    if len(s3) != len(s2) + len(s1):
        return False
    # dp[i][j] = (dp[i-1][j] && s3[i+j-1] == s1[i-1]) || (dp[i][j-1] && s2[j-1] == s3[i+j-1])
    dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    dp[0][0] = True

    # 第一行
    for j in range(len(s2)):
        dp[0][j + 1] = (dp[0][j] and s2[j] == s3[j])

    # 第一列
    for i in range(len(s1)):
        dp[i + 1][0] = (dp[i][0] and s1[i] == s3[i])
    # print(dp)

    for i in range(len(s1)):
        for j in range(len(s2)):
            dp[i + 1][j + 1] = (dp[i + 1][j] and s2[j] == s3[i + j + 1]) or (
                    dp[i][j + 1] and s1[i] == s3[i + j + 1])
    # print(dp)
    return dp[-1][-1]
