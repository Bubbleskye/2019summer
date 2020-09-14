class Solution:
    def wordsAbbreviation(self, dict):
        from collections import defaultdict
        lookup = defaultdict(list)
        # print(sorted(dict))
        res = [None for _ in range(len(dict))]

        def abbreviate(word, k):
            n = len(word)
            if n <= 3:
                return word
            tmp_word = word[:k] + str(n - k - 1) + word[-1]
            if len(tmp_word) < n:
                return tmp_word
            else:
                return word
        # pre是前面字符的个数 先设定除第一个字符和最后一个字符全都用数字统计
        pre = 1
        for idx, word in enumerate(dict):
            # print(idx,word)
            lookup[abbreviate(word, 1)].append([word, idx])
        # 处理重复缩写的单词
        pre = pre + 1
        #print(lookup)
        while lookup:
            # print(lookup)
            next_lookup = defaultdict(list)
            for key, item in lookup.items():
                if len(item) == 1:
                    res[item[0][1]] = key
                else:
                    # 重复缩写的重新建立缩写
                    for w, idx in item:
                        abb = abbreviate(w, pre)
                        # print(abb)
                        next_lookup[abb].append([w, idx])
            pre = pre + 1
            lookup = next_lookup

        return res