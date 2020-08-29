def findCelebrity(self, n: int) -> int:
    for i in range(n):
        flag = 0
        for j in range(n):
            if not knows(j, i) or (i != j and knows(i, j)):
                flag = 1
                break
        if flag == 0:
            return i
    return -1

# 判断i不是名人即跳出