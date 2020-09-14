def findCelebrity(self, n: int) -> int:
    for i in range(n):
        # 检查i是否是名人：i不认识所有人/但所有人都认识i
        flag = 0
        for j in range(n):
            if not knows(j, i) or (i != j and knows(i, j)):
                # j不认识i 或者i认识j 说明i不是名人
                flag = 1
                break
        if flag == 0:
            return i
    return -1

# 判断i不是名人即跳出