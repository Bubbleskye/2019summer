# 如果将单词列表里的每个单词看作一个个节点，如果一个单词能通过只改变一个字母变成另一个单词，那么这2个单词直接应该形成一条边，表示可以互相到达。
# 把开始单词当作开始节点，结束单词当作结束节点，现在要解决的问题就是开始节点和结束节点是否有连接，求最短路径。
# 首先，如果结束单词一开始就不在单词列表里，可以直接返回，因为本身就不存在这样的节点。
# 其次，求最短路径，最容易想到的就是BFS解法，这个从起始节点开始遍历，如果找到了结束节点，代表找到了结果，同时这个肯定是最优解（路径最短）。
# 注意：此时我们并不能直接返回答案，因为要求的所有最短路径，所以我们要把这一层的所有满足结果都返回。
#
def findLadders(beginWord, endWord, wordList) :
    from collections import deque
    se = set(wordList)
    if endWord not in se:
        return 0

    def edges(word):
        # 遍历找出只改变一个字母的在字典中的所有选择
        generateword = set()
        arr = list(word)
        for i in range(len(arr)):
            c = arr[i]
            for j in range(97, 123):
                arr[i] = chr(j)
                newWord = ''.join(arr)
                if newWord in se and newWord not in marked:
                    # 已经出现过，再回去路径肯定更长
                    generateword.add(newWord)
            arr[i] = c
        return generateword

    res = []
    marked = set()
    step = 1
    # marker记录已经走过的路径
    queue = deque()
    queue.append([beginWord])
    # queue中存的是路径
    while queue:
        step = step + 1
        flag = False
        for _ in range(len(queue)):
            wordlist = queue.popleft()
            found = False
            nowword = wordlist[-1]
            marked.add(nowword)  # 每次把出现过的单词放入marked
            generateword = edges(nowword)
            if generateword:
                flag = True
                for w in generateword:
                    if w == endWord:
                        res.append(wordlist + [w])
                        found = True
                    queue.append(wordlist + [w])
            if found:  # 找到就不再遍历了，即使再有endWord，路径也会更长
                break
        if found:
            break
        if not flag:
            return 0
    if found:
        return step
    else:
        return 0


beginWord="hot"
endWord="dog"
wordList=["hot","dog"]
print(findLadders(beginWord, endWord, wordList))