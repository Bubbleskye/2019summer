class Solution:
    def __init__(self):
        self.count=0
    def maxAreaOfIsland(grid):
        if not grid:
            return 0
        maxs=[]
        row=len(grid)
        col=len(grid[0])
        direction=[[1,0],[-1,0],[0,1],[0,-1]]
        dp=[[False for _ in range(col)] for _ in range(row)]
        def Island(i,j,dp):
            dp[i][j]=True
            for d in direction:
                newi=i+d[0]
                newj=j+d[1]
                if newi>=0 and newi<row and newj>=0 and newj<col and grid[newi][newj]==1 and dp[newi][newj]==False:
                    self.count=self.count+1
                    Island(newi,newj,dp)
            return

        for i in range(row):
            for j in range(col):
                if grid[i][j]==1 and dp[i][j] == False:
                    self.count=1
                    Island(i,j,dp)
                    maxs.append(self.count)
        if len(maxs)==0:
            return 0
        return max(maxs)