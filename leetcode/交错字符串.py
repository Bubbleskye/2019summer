def isInterleave(s1, s2, s3):
    if len(s3) != len(s2) + len(s1):
        return False
    # 索引为0的是前1个字符，所以存在一个差
    # dp[i][j] = (dp[i-1][j] && s3[i+j-1] == s1[i-1]) || (dp[i][j-1] && s2[j-1] == s3[i+j-1])
    # s1的前i个字符与s2的前j个字符是否能组成s3的前i+j个字符
    # 前0个元素即为空，所以长度为n的元素即要到前n个字符
    dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    dp[0][0] = True

    # 第一行 s1取前0个字符 完全看s2
    for j in range(len(s2)):
        dp[0][j + 1] = (dp[0][j] and s2[j] == s3[j])

    # 第一列 s2取前0个字符 完全看s1
    for i in range(len(s1)):
        dp[i + 1][0] = (dp[i][0] and s1[i] == s3[i])
    # print(dp)

    for i in range(len(s1)):
        for j in range(len(s2)):
            dp[i + 1][j + 1] = (dp[i + 1][j] and s2[j] == s3[i + j - 1] ) or (
                    dp[i][j + 1] and s1[i] == s3[i + j - 1])
    # print(dp)
    return dp[-1][-1]
