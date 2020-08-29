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
            return word
        # pre是前面字符的个数
        pre = 1
        for idx, word in enumerate(dict):
            # print(idx,word)
            lookup[abbreviate(word, 1)].append([word, idx])
        pre += 1
        #print(lookup)
        while lookup:
            # print(lookup)
            next_lookup = defaultdict(list)
            for key, item in lookup.items():
                if len(item) == 1:
                    res[item[0][1]] = key
                else:
                    # print(item)
                    for w, idx in item:
                        abb = abbreviate(w, pre)
                        # print(abb)
                        next_lookup[abb].append([w, idx])

            pre += 1
            lookup = next_lookup

        return res