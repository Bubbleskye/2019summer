def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 1:
        return 1
    else:
        dp = [0]
        letter = []
        for i in range(1, len(s) + 1):
            if s[i - 1] not in letter:
                dp.append(dp[i - 1] + 1)
                letter.append(s[i - 1])
            else:
                dp.append(dp[i - 1] - (letter.index(s[i - 1]) + 1) + 1)
                letter = letter[letter.index(s[i - 1]) + 1:]
                letter.append(s[i - 1])
        return max(dp)

s="uqinntq"
A=lengthOfLongestSubstring(s)
print(A)

# 最长不重复子串
# 与053的区别在于这道题需要满足不重复
# 所以不能采用分治算法，而是采用动态规划
# 如果没有出现过dp[i]=dp[i-1]+1  ；  如果出现过则剪掉出现的之前的字符串，重新创建字符串