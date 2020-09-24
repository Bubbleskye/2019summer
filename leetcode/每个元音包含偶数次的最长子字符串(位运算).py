s = "aeeaaeea"
dp = [-float('inf') for _ in range(33)]
# dp中储存的是此时字符串的二进制pattern的末尾字符位置i
# 首先初始化 dp 长度为 32，对应了 5 个元音每个次数或奇或偶一共 2^5=32 种状态
dp[0] = -1
pattern = 0
res = 0
# a=00001 e=00010 i=00100 o=01000 u=10000
# 其中 0 表示对应元音出现了偶数次数，1 表示奇数
# 位运算异或：不同输出1 相同输出0
for i in range(len(s)):
    if s[i] == 'a':
        pattern = pattern ^(1<<0)
    elif s[i] == 'e':
        pattern = pattern ^(1<<1)
    elif s[i] == 'i':
        pattern = pattern ^(1<<2)
    elif s[i] == 'o':
        pattern = pattern ^(1<<3)
    elif s[i] == 'u':
        pattern = pattern ^(1<<4)

    if dp[pattern] != -float('inf'):
        # 如果这个模式（存在1）前面出现过，不改变dp对应的值，始终记录最小的那个
        # 或者pattern是全0，则找到dp[0]=-1
        cur_len = i-dp[pattern]
        res = max(res,cur_len)
    else:
        dp[pattern] = i
print(res)