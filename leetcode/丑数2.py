# 弹出堆中最小的丑数 k,并在堆中添加三个丑数：k×2, k×3，和k×5。
# 弹出的第n个丑数 即为从小到大第n个
n=10
if n==1:
    print(1)
import heapq
heap=[1]
count=0
while count<n:
    tmp=heapq.heappop(heap)
    if tmp*2 not in heap:
         heapq.heappush(heap,tmp*2)
    if tmp*3 not in heap:
        heapq.heappush(heap,tmp*3)
    if tmp*5 not in heap:
        heapq.heappush(heap,tmp*5)
    count=count+1
print(tmp)