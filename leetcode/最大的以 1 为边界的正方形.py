def largest1BorderedSquare(grid):
    r, c = len(grid), len(grid[0])
    h, v = [a[:] for a in grid], [a[:] for a in grid]
    # 通过两个矩阵存储每个点的上面v和左边h有多少个连续的1(包括自己)
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                if i:
                    v[i][j] = v[i - 1][j] + 1
                if j:
                    h[i][j] = h[i][j - 1] + 1

    for k in range(min(r, c), 0, -1):
        # k是边长
        for i in range(r - k + 1):
            for j in range(c - k + 1):
                # [i,j]为左上角
                if min(v[i + k - 1][j], v[i + k - 1][j + k - 1], h[i][j + k - 1], h[i + k - 1][j + k - 1]) >= k:
                    # v[i + k - 1][j]左下角的上面/v[i + k - 1][j + k - 1]右下角的上面/ h[i + k - 1][j + k - 1]右上角的左边
                    return k ** 2
    return 0

grid = [[1,1,1],[1,0,1],[1,1,1]]
print(largest1BorderedSquare(grid))