def addBoldTag(s, dict):
    lookup = set()
    for d in dict:
        left = 0
        while True:
            # 通过循环找到d的所有位置索引
            loc = s.find(d, left)
            if loc == -1:
                break
            for i in range(loc, loc + len(d)):
                if i not in lookup:
                    lookup.add(i)
            left = loc + 1
    # lookup统计出字典中字符在s中的索引位置
    res = ""
    i = 0
    while i < len(s):
        left=i
        while i < len(s) and i in lookup:
            i = i + 1
        if left == i:
            # 即i处字符不在dict中
            res = res + s[i]
            i = i + 1

        else:
            res = res + "<b>"
            for j in range(left, i):
                res = res + s[j]
            res = res + "</b>"
    #         字符在dict中，则left记录字符串的左端，i记录字符串的右端
    return res

s = "abcxyz123"
dict = ["abc","123"]
print(addBoldTag(s, dict))