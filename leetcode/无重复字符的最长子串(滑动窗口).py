def lengthOfLongestSubstring(s):
    if not s:
        return 0
    res = 1
    dict = {}
    left = 0
    right = left
    while right < len(s):
        if s[right] not in dict:
            dict[s[right]] = right
            right = right + 1
        else:
            res = max(res, right - 1 - left + 1)
            index = dict[s[right]]
            while left <= index:
                dict.pop(s[left])
                left = left + 1
    res = res = max(res, right - 1 - left + 1)
    return res

s="uqinntq"
A=lengthOfLongestSubstring(s)
print(A)
