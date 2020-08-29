# 多源广度优先搜索
# 第一层的0全部读进去，从0出发
def updateMatrix(matrix):
    res = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    from collections import deque
    queue = deque()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                queue.append([i, j])
                res[i][j] = 0
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    layer = 0
    while queue:
        layer = layer + 1
        for _ in range(len(queue)):
            point = queue.popleft()
            for d in direction:
                newx = point[0] + d[0]
                newy = point[1] + d[1]
                if newx >= 0 and newx < len(matrix) and newy >= 0 and newy < len(matrix[0]) and matrix[newx][newy] == 1 and res[newx][newy] == -1:
                    res[newx][newy] = layer
                    queue.append([newx, newy])
    return res