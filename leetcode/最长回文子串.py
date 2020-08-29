# def longestPalindrome(s):
#     # 状态方程 给定首尾元素i，j
#     # dp[i,j]=dp[i+1,j-1] and s[i]==s[j]
#     # 循环从末尾开始,保证dp[i+1,j-1]已经判断过
#     if len(s) <= 1:
#         return s
#     dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
#     maxlen = 1
#     start = 0
#     for j in range(0, len(s)):
#         for i in range(0, j):
#             if (dp[i + 1][j - 1] != 0 or j - i < 3) and s[i] == s[j]:
#                 dp[i][j] = j - i + 1
#                 if dp[i][j] > maxlen:
#                     maxlen = int(dp[i][j])
#                     start = i
#     return s[start:start + maxlen]

def longestPalindrome(s):
    # dp[i,j]以i为头j为尾的最长回文子串
    # dp[i][j]=dp[i+1][j-1] and s[i]==s[j]
    maxl = 0
    dp = [[False for _ in range(len(s))] for _ in range(len(s))]
    for j in range(len(s)):
        for i in range(0, j + 1, 1):
            if i == j:
                dp[i][j] = True
                if j - i + 1 > maxl:
                    maxl = j - i + 1
                    maxs = s[i:j+1]
            elif j - i == 1 and s[i] == s[j]:
                dp[i][j] = True
                if j - i + 1 > maxl:
                    maxl = j - i + 1
                    maxs = s[i:j+1]
            elif dp[i + 1][j - 1] and s[i] == s[j]:
                dp[i][j] = True
                if j - i + 1 > maxl:
                    maxl = j - i + 1
                    maxs = s[i:j+1]
            else:
                continue
    return maxs

s="zgtklhfzomzjckwmluvivvcmhjrwkuvcjrxojobpdedpamdshcwwsetfbacvonecrdvugeibglvhxuymjvoryqjwullvzglqazxrdmczyvbgakjagttrezmvrlptiwoqkrtxuroeqmryzsgokopxxdpbejmtwvpnaqrgqladdszhdwxfckmewhdvihgvacueqhvwvjxoitlpfrckxkuksaqzjpwgoldyhugsacflcdqhifldoaphgdbhaciixouavqxwlghadmfortqacbffqzocinvuqpjthgekunjsstukeiffjipzzabkuiueqnjgkuiojwbjzfynafnlcaryygqjfixaoeowhkxkbsnpsvnbxuywfxbnuoemxynbtgkqtjvzqikbafjnpbeirxxrohhnjqrbqqzercqcrcswojyylunuevtdhamlkzqnjrzibwckbkiygysuaxpjrgjmurrohkhvjpmwmmtpcszpihcntyivrjplhyrqftghglkvqeidyhtmrlcljngeyaefxnywpfsualufjwnffyqnpitgkkyrbwccqggycrvoocbwsdbftkigrkcbojuwwctknzzmvhbhbfzrqwzllulbabztqnznkqdyoqnrxhwavqhzyzvmmmphzxbikpharseywpfsqyybkynwbdrgfsaxduxojcdqcjuaywzbvdjgjqtoffasiuhvxcaockebkuxpiomqmtvsqhnyxfjceqevqvnapbk"
print(len(s))
print(longestPalindrome(s))