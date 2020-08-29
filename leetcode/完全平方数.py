# import numpy as np
# # n=48
# # key=int(np.sqrt(n))
# # if key**2==n:
# #     print(1)
# # res=[]
# # def dfs(n,count,res):
# #     if n<4:
# #         res.append(count+n)
# #         return res
# #     key=int(np.sqrt(n))
# #     for j in range(key,1,-1):
# #         count=count+1
# #         dfs(n-j**2,count,res)
# #         count = count - 1
# #
# # for i in range(key,1,-1):
# #     count=0
# #     count=count+1
# #     dfs(n-i**2,count,res)
# # print(min(res))
# 超时___回溯

# import numpy as np
# n=48
# if n == 1:
#     print(1)
# if n == 2:
#     print(2)
# if n == 3:
#     print(3)
# dp=[1 for i in range(n+1)]
# dp[2]=2
# dp[3]=3
# for i in range(4,n+1):
#     res=[]
#     key = int(np.sqrt(i))
#     if pow(key,2)==i:
#         dp[i]=1
#     else:
#         for j in range(key, 1, -1):
#             res.append(dp[pow(j,2)]+dp[i-pow(j,2)])
#         dp[i]=min(res)
# print(dp[n])
# 超时__动态规划__dp[pow(j,2)]+dp[i-pow(j,2)]

# 广度优先遍历
from collections import deque
import numpy as np
n=12
# deque模块 在两端都可以操作
queue = deque([n])
step = 0
visited = set()
# set() 函数创建一个无序不重复元素集
while queue:
    step = step + 1
    l = len(queue)
    for _ in range(l):
        tmp = queue.pop()
        # pop()抛出最后一个元素
        for i in range(1, int(np.sqrt(tmp))+1):
            x = tmp - pow(i,2)
            if (x == 0):
                print(step)
            if (x not in visited):
                queue.appendleft(x)
                # .appendleft从左侧加入数据
                visited.add(x)
#             如果x in visited 则不用再考虑这条路,因为他之前已经出现过,这条路的结果一定时大于等于前面那条路的
print(step)