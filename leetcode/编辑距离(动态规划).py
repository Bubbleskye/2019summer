word1="horse"
word2="ros"
# dp[i][j] 代表 word1 前i个字符word1[:i]转换成 word2 前j个字符word2[:j]需要最少步数
# 存在前0个字符,即为空字符
# 当 word1[i] == word2[j]，dp[i][j] = dp[i-1][j-1]；
# 当 word1[i] != word2[j]，dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
# 其中，dp[i-1][j-1] 表示替换操作当word1中的前i-1个就可以变换为word2中的前j-1个时,将word1中第i个字符替换掉
# dp[i-1][j] 表示删除word1操作(当word1中的前i-1个就可以变换为word2中的前j个时，我们需要将word1中的第i个字符删除
# dp[i][j-1] 表示word1插入操作(当word1中的前i个可以变换为word2中的前j-1个时，我们需要将word1中的第i个字符后面增加一个
dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
dp[0][0]=0
# 第一行,word1前0个字符,转为word2前j个字符
for j in range(1,len(word2)+1):
    dp[0][j] = dp[0][j - 1] + 1
# 第一列,word2前0个字符,转为word1前i个字符
for i in range(1,len(word1)+1):
    dp[i][0] = dp[i - 1][0] + 1
for i in range(len(word1)):
    for j in range(len(word2)):
        if word1[i] == word2[j]:
            dp[i+1][j+1] = dp[i][j]
        else:
            dp[i+1][j+1] = min(dp[i][j],dp[i][j+1], dp[i+1][j]) + 1
print(dp[-1][-1])