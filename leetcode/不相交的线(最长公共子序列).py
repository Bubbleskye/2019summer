def maxUncrossedLines(A, B):
    # 本质：最长公共子序列
    # 子序列不用连续，只要相对位置一样就行
    # dp[i][j] A子串到i与B子串到j时，公共子序列长度
    if not A or not B:
        return 0
    dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1], dp[i][j])
    return dp[-1][-1]