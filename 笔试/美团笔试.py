# n=5
# grid=[['.', '.', 'X', '.', 'X'], ['X', 'X', '.', '.', '.']]
def road(n,grid):
    row=2
    col=n
    dp=[[0 for _ in range(col)] for _ in range(row)]
    if grid[-1][-1]=="X" or grid[0][0]=="X":
        return -1
    dp[0][0]=1
    # for i in range(row):
    #     for j in range(col):
    #         if grid[i][j]=="X":
    #             dp[i][j]=0
    for j in range(col):
        for i in range(row):
            if grid[i][j]==".":
                if j-1>=0 and i==0:
                    dp[i][j]=dp[i][j-1]+dp[i+1][j-1]
                elif j-1>=0 and i==1:
                    dp[i][j]=dp[i][j-1]+dp[i-1][j-1]
    if dp[-1][-1]!=0:
        return dp[-1][-1]
    else:
        return -1

# 输入是字符串，拆分后，一个个字符存入列表
# 也可以直接list(input()),将一个连续的字符串拆分成元素为字母的列表
# ','.join(input()),将一个字符串拆分为元素为字母的字符串
if __name__ == "__main__":
    import sys
    n=int(input())
    mx=[]
    for i in range(2):
        m = input().split("\n")
        mx.append(m)
    grid=[]
    for i in range(2):
        line=str(mx[i])[2:n+2]
        lines=[]
        for j in range(len(line)):
            lines.append(line[j])
        grid.append(lines)
    cnt = road(n, grid)
    print(cnt)



