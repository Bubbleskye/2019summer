# 由空地和墙组成的迷宫中有一个球。球可以向上下左右四个方向滚动，但在遇到墙壁前不会停止滚动。当球停下时，可以选择下一个方向。
# 给定球的起始位置，目的地和迷宫，找出让球停在目的地的最短距离。距离的定义是球从起始位置（不包括）到目的地（包括）经过的空地个数。如果球无法停在目的地，返回 -1。
# 迷宫由一个0和1的二维数组表示。 1表示墙壁，0表示空地。你可以假定迷宫的边缘都是墙壁。起始位置和目的地的坐标通过行号和列号给出。
# 输入 1: 迷宫由以下二维数组表示
#
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
#
# 输入 2: 起始位置坐标 (rowStart, colStart) = (0, 4)
# 输入 3: 目的地坐标 (rowDest, colDest) = (4, 4)
#
# 输出: 12
#
# 解析: 一条最短路径 : left -> down -> left -> down -> right -> down -> right。
#              总距离为 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12。


##寻找最短路径的方法：1、各个路径的代价权重不一样，要用dij算法 2、各个路径权重一样，用广度优先搜索

# dijkstra算法+堆heap优化
# 从heap中pop出的点是已经找到从起点出发最近距离的点，在用这个点更新周围点的距离。这个点，之后不再考虑。
# 对于已经得到最短距离的点，以后不再访问，存入visited。对于同一个点，越早出现的最小值越小。
def shortestDistance(maze, start, destination):
    import heapq
    row = len(maze)
    col = len(maze[0])
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    start, destination = tuple(start), tuple(destination)
    heap = [(0, start)]
    visited = set()
    while heap:
        dis, loc = heapq.heappop(heap)
        # 当终点被pop出来，才算是找到了最近的到终点的路径
        if loc == destination:
            return dis
        visited.add(loc)
        for d in direction:
            dx, dy = d
            x, y = loc
            length = 0
            # 利用while循环，不是每走一步都要加到队列中，而是要撞到墙了才要加入队列中
            # 在过程中可以路过之前已经确定最小值的点
            while x + dx >= 0 and x + dx < row and y + dy >= 0 and y + dy < col and maze[x + dx][y + dy] == 0:
                x, y = x + dx, y + dy
                length = length + 1

            # 将不满足循环条件的前一步的坐标加入队列
            # 如果已经在visited中，说明从起点到该点的最短距离已经得到，则不再考虑
            if (x, y) not in visited:
                heapq.heappush(heap, (dis + length, (x, y)))
    return -1

maze=[[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start=[0,4]
destination=[4,4]
print(shortestDistance(maze, start, destination))