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

