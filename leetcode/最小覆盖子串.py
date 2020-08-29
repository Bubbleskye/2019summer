def minWindow(s, t):
    if not s:
        return ""
    from collections import Counter
    t = Counter(t)
    lookup = Counter()
    start = 0
    end = 0
    min_len = float("inf")
    res = ""
    while end < len(s):
        lookup[s[end]] += 1
        end += 1
        # print(start, end)
        while all(map(lambda x: lookup[x] >= t[x], t.keys())):
            # 利用all函数 用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False
            # map(function函数, iterable序列) 参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表
            if end - start < min_len:
                res = s[start:end]
                min_len = end - start
            lookup[s[start]] -= 1
            start += 1
    return res

s="ADOBECODEBANC"
t="ABC"
print(minWindow(s, t))