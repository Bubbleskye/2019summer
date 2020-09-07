def solveNQueens(n):
    # 按行依次放置，所以只用考虑列/两条斜线
    # 两条斜线，从左上到右下的row-col值固定，从右上到左下的row+col值固定
    def generateBoard():
        board = []
        for i in range(n):
            row[queens[i]] = "Q"
            board.append("".join(row))
            # 恢复row字符串
            row[queens[i]] = "."
        return board

    def backtrack(row):
        if row == n:
            board = generateBoard()
            solutions.append(board)
            return
        else:
            for col in range(n):
                if col in columns or row - col in diagonal1 or row + col in diagonal2:
                    continue
                # queens中是第row行在第col列放一个皇后
                queens[row] = col
                columns.add(col)
                diagonal1.add(row - col)
                diagonal2.add(row + col)
                backtrack(row + 1)
                # 回溯return后的恢复
                queens[row] = -1
                columns.remove(col)
                diagonal1.remove(row - col)
                diagonal2.remove(row + col)

    solutions = []
    queens = [-1 for _ in range(n)]
    columns = set()
    diagonal1 = set()
    diagonal2 = set()
    row = ["."] * n
    backtrack(0)
    return solutions