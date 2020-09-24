def minWindow(s, t):
    def twodict(dict,target):
        # 判断target字典中的元素是否在dict中，且个数>=target中
        for k,v in target.items():
            if k in dict and dict[k]>=v:
                continue
            else:
                return False
        return True
    need = {}
    for c in t:
        if c not in need:
            need[c] = 1
        else:
            need[c] = need[c] + 1
    lookup = {}
    start = 0
    end = 0
    min_len = float("inf")
    res = ""
    while end < len(s):
        lookup[s[end]]=lookup.get(s[end],0)+1
        # print(start, end)
        while twodict(lookup,need):
            # 如果此时的字符串包含目标子串，移动左指针，缩小子串长度，减去左边的字符
            if end - start < min_len:
                res = s[start:end+1]
                min_len = end +1 - start
            lookup[s[start]] = lookup[s[start]] - 1
            start = start + 1
        # 如果此时的字符串不包含目标子串，则移动右指针
        end = end + 1
    return res

s="ADOBECODEBANC"
t="ABC"
print(minWindow(s, t))