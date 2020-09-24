from collections import deque
coins=[278,274,153,490]
amount=8633
def coinChange(coins,amount):
    queue = deque([amount])
    appear = set()
    count = 0
    while queue:
        count=count+1
        l = len(queue)
        for _ in range(l):
            tmp = queue.pop()
            for coin in coins:
                lastamount = tmp - coin
                if lastamount == 0:
                    return count
                if lastamount not in appear and lastamount>0:
                    queue.appendleft(lastamount)
                    appear.add(lastamount)
    return -1
print(coinChange(coins,amount))
# 用set.add()比list.append()省时


# 动态规划
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         if amount==0:
#             return 0
#         dp=[float("inf") for _ in range(amount+1)]
#         for c in coins:
#             if c<=amount:
#                 dp[c]=1
#         for i in range(1,amount+1):
#             if dp[i]==float("inf"):
#                 for c in coins:
#                     if i-c>=0:
#                         dp[i]=min(dp[i],dp[i-c]+1)
#         if dp[-1]!=float("inf"):
#             return dp[-1]
#         else:
#             return -1

