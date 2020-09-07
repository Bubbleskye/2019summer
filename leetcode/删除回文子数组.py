def minimumMoves(arr):
    # 回文子数组即是连续的一段
    # dp[i][j]删除arr[i:j+1]这一段所需要进行的操作次数
    # if arr[i]==arr[j]: dp[i][j]=dp[i+1][j-1]
    # 如果头尾相同的话，这两个字符不用单独算一次删除，这两个字符只要跟着中间的随便哪个组合一起删掉就可以
    # else: dp[i][j]=min(dp[i][k]+dp[k+1][j])
    # 如果头尾不相同的话，分两段逐个找最小
    dp = [[float("inf") for _ in range(len(arr))] for _ in range(len(arr))]
    for j in range(len(arr)):
        for i in range(j, -1, -1):
            if i == j:
                dp[i][j] = 1
            elif i + 1 == j and arr[i] == arr[j]:
                dp[i][j] = 1
            elif i + 1 == j and arr[i] != arr[j]:
                dp[i][j] = 2
            else:
                if arr[i]==arr[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
    return dp[0][-1]
arr = [1,3,4,1,5]
print(minimumMoves(arr))