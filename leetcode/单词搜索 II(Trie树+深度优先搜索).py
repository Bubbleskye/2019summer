import copy
class Solution:
    def __init__(self):
        self.dict = {}
        self.res = []
    # 建立Trie树来存储words
    def findWords(self, board, words):
        def insert(word, index):
            tmp = self.dict
            for i in range(len(word)):
                if word[i] not in tmp:
                    tmp[word[i]] = {}
                tmp = tmp[word[i]]
            tmp["end"] = index

        for i in range(len(words)):
            insert(words[i], i)
        print(self.dict)

        def backtrack(x, y, tmpdict, flag):
            for d in direction:
                newx = x + d[0]
                newy = y + d[1]
                if 0 <= newx < len(board) and 0 <= newy < len(board[0]) and flag[newx][newy] == False and board[newx][
                    newy] in tmpdict:
                    # 重点
                    # 在回溯中，由于二维列表的原因，当你更改了其中的一个值，所有的二维列表中的相应值都会更改
                    # 即使结束一层回溯，回到上一层，二位列表的状态也发生了改变
                    # 所以这里在backtrack中传参数时，不能传递原来的二位列表，而应该对二位列表进行deepcopy后传入
                    # 这样在之后的层中以前层的状态也被copy进去了，而之后层做的修改，并不会影响到之前层（因为是两个不同的变量）
                    # 当一层回溯结束回到上一层，仍是之前的状态
                    tmpflag = copy.deepcopy(flag)
                    tmpflag[newx][newy] = True
                    backtrack(newx, newy, tmpdict[board[newx][newy]], tmpflag)
            if "end" in tmpdict and words[tmpdict["end"]] not in self.res:
                self.res.append(words[tmpdict["end"]])
            else:
                return

        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in self.dict:
                    flag = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
                    flag[i][j] = True
                    tmpdict = self.dict[board[i][j]]
                    if "end" in tmpdict and words[tmpdict["end"]] not in self.res:
                        self.res.append(words[tmpdict["end"]])
                    for d in direction:
                        newx = i + d[0]
                        newy = j + d[1]
                        if 0 <= newx < len(board) and 0 <= newy < len(board[0]) and flag[newx][newy] == False and \
                                board[newx][newy] in tmpdict:
                            tmpflag=copy.deepcopy(flag)
                            tmpflag[newx][newy] = True
                            backtrack(newx, newy, tmpdict[board[newx][newy]], tmpflag)
        return self.res

board=[["a","b","c"],["a","e","d"],["a","f","g"]]
words=["eaabcdgfa"]
solution=Solution()
print(solution.findWords(board, words))
