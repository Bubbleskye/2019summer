grid=[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
# 偏移
row=len(grid)
if row == 0:
    print(0)
col=len(grid[0])
count=0
marked = [[False for _ in range(col)] for _ in range(row)]
def dfs(grid, i, j, row, col, marked):
    marked[i][j] = True
    for direction in directions:
        new_i = i + direction[0]
        new_j = j + direction[1]
        if 0 <= new_i < row and 0 <= new_j < col and not marked[new_i][new_j] and grid[new_i][new_j] == '1':
            dfs(grid, new_i, new_j, row, col, marked)
    return

# 从第 1 行、第 1 格开始，对每一格尝试进行一次 DFS 操作
for i in range(row):
    for j in range(col):
        # 只要是陆地，且没有被访问过的，就可以使用 DFS 发现与之相连的陆地，并进行标记
        if not marked[i][j] and grid[i][j] == '1':
            # count 可以理解为连通分量，你可以在深度优先遍历完成以后，再计数，
            count = count+1
            dfs(grid, i, j, row, col, marked)
print(count)