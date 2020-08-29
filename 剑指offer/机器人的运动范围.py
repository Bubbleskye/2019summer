def movingCount(threshold, rows, cols):
    # write code here
    if threshold < 0:
        return 0

    def digitnum(i):
        sum = 0
        while i > 0:
            sum = sum + i % 10
            i = int(i / 10)
        return sum

    def backtrack(i, j, rows, cols, flag, threshold):
        if i < 0 or i >= rows or j < 0 or j >= cols or digitnum(i) + digitnum(j) > threshold or flag[i][j] == 1:
            return 0
        flag[i][j] = 1
        return 1 + backtrack(i - 1, j, rows, cols, flag, threshold)+backtrack(i + 1, j, rows, cols, flag, threshold)+backtrack(i, j - 1, rows, cols, flag, threshold)+backtrack(i, j + 1, rows, cols, flag, threshold)
    flag = [[0 for _ in range(cols)] for _ in range(rows)]
    return backtrack(0, 0, rows, cols, flag, threshold)




print(movingCount(10, 1, 100))