def shortestPalindrome(s):
    if not s:
        return ""
    n = len(s)
    revs = s[::-1]
    # 通过翻转来比对回文串的位置
    for i in range(len(s)):
        if revs[i:] == s[:n - i]:
            return revs[:i] + s