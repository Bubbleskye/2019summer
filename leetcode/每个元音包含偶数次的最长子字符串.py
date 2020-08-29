s = "eleetminicoworoep"
dp = [-float('inf')]*32
# dp中储存的是此时二进制表示的字符串的末尾字符位置i
# 首先初始化 dp 长度为 32，对应了 5 个元音每个次数或奇或偶一共 2^5=32 种状态
dp[0] = -1
pattern = 0
res = 0
# a=00001 e=00010 i=00100 o=01000 u=10000
# 位运算 异或
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
        cur_len = i-dp[pattern]
        res = max(res,cur_len)
    else:
        dp[pattern] = i
print(res)
