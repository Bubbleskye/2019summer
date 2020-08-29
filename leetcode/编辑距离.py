word1="horse"
word2="ros"
# dp[i][j] 代表 word1 到 i 位置转换成 word2 到 j 位置需要最少步数
# 当 word1[i] == word2[j]，dp[i][j] = dp[i-1][j-1]；
# 当 word1[i] != word2[j]，dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
# 其中，dp[i-1][j-1] 表示替换操作当word1中的前i-1个就可以变换为word2中的前j-1个时,将word1z中第i个字符替换掉
# dp[i-1][j] 表示删除word1操作(当word1中的前i-1个就可以变换为word2中的前j个时，我们需要将word1中的第i个字符删除
# dp[i][j-1] 表示word1插入操作(当word1中的前i个可以变换为word2中的前j-1个时，我们需要将word1中的第i个字符后面增加一个
dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
# 第一行
for j in range(1,len(word2)+1):
    dp[0][j] = dp[0][j - 1] + 1
# 第一列
for i in range(1,len(word1)+1):
    dp[i][0] = dp[i - 1][0] + 1
for i in range(len(word1)):
    for j in range(len(word2)):
        if word1[i] == word2[j]:
            dp[i+1][j+1] = dp[i][j]
        else:
            dp[i+1][j+1] = min(dp[i][j],dp[i][j+1], dp[i+1][j]) + 1
print(dp[-1][-1])