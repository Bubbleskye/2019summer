def maxDistance(grid):
    # 即求出每一个海洋区域（grid[i][j] == 0 的区域）的「最近陆地区域」，然后记录下它们的距离，然后在这些距离里面取一个最大值。
    # 但会超时
    # 选择优化方法
    # 将所有陆地加入队列，而不是海洋。广度优先搜索，先找到所有距离陆地为1的点，在从1点继续找。并不断更新最终答案为最大值
    from collections import deque
    row = len(grid)
    col = len(grid[0])
    if sum(map(sum, grid)) == 0 or sum(map(sum, grid)) == row * col:
        return -1
    dis=[[float("inf") for _ in range(col)] for _ in range(row)]
    flag = [[False for _ in range(col)] for _ in range(row)]
    queue = deque([])
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                dis[i][j]=0
                queue.append([i,j])
                flag[i][j]=True
    ans = 0
    direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while queue:
        for _ in range(len(queue)):
            [x, y] = queue.popleft()
            for d in direction:
                newx = x + d[0]
                newy = y + d[1]
                if newx >= 0 and newx < row and newy >= 0 and newy < col and not flag[newx][newy]:
                    # 之前访问过，说明之前的距离肯定是最小距离。越后访问，距离越大
                    dis[newx][newy] = min(dis[newx][newy],dis[x][y]+1)
                    ans = max(ans, dis[newx][newy])  # 更新答案
                    flag[newx][newy] = True
                    queue.append([newx, newy])
    return ans

grid=[[1,0,0],[0,0,0],[0,0,0]]
print(maxDistance(grid))