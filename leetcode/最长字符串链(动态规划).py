words=["a","ba","bca","bdca"]
words = sorted(words, key=lambda i: len(i))
# 按照单词长度排序
note={}
# 字典中存储以该key单词为末尾的最长字符串链长度
maxChain=1
for word in words:
    if word not in note:
        note[word]=1
    for i in range(0,len(word)):
        newWord=word[:i]+word[i+1:]
        # 去掉第i个字符
        if (newWord) in note:
            note[word]=max(note[word],note[newWord]+1)
    maxChain=max(maxChain,note[word])
print(maxChain)
# 每次去掉一个字符，挨个比较