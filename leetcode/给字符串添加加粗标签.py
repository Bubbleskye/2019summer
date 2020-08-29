def addBoldTag(s, dict):
    lookup = set()
    for d in dict:
        left = 0
        while True:
            loc = s.find(d, left)
            if loc == -1:
                break
            for i in range(loc, loc + len(d)):
                lookup.add(i)
            left = loc + 1
    # lookup统计出字典中字符在s中的索引位置
    res = ""
    i = 0
    while i < len(s):
        left = i
        while i < len(s) and i in lookup:
            i = i + 1
        if left == i:
            res = res + s[i]
            i = i + 1
        #     即i处字符不在dict中
        else:
            res += "<b>"
            for j in range(left, i):
                res = res + s[j]
            res = res + "</b>"
    #         字符在dict中，则left记录字符串的左端，i记录字符串的右端
    return res

s = "abcxyz123"
dict = ["abc","123"]
print(addBoldTag(s, dict))