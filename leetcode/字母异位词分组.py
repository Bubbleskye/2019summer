# 最简单的，排序，如果是同一个单词，那么就是组成一样的
# 比如 “eat” "tea" 排序后都为 “aet”

# 字符串排序
# l=list('eat')
# l.sort()
# print("".join(l))
# aet

strs=["eat", "tea", "tan", "ate", "nat", "bat"]
dict = {}
for i in range(len(strs)):
    l = list(strs[i])
    l.sort()
    key = "".join(l)
    # key=sorted(strs[i])
    if key not in dict:
        dict[key] = [strs[i]]
    else:
        dict[key] = dict[key] + [strs[i]]
print(dict)
res=[]
# 遍历字典的值
for value in dict.values():
    res.append(value)
print(res)