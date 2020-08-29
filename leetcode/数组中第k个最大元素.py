import heapq
nums=[3,2,3,1,2,4,5,5,6]
k=4
heap = []
for i in range(len(nums)):
    heapq.heappush(heap, -nums[i])
while k:
    item = heapq.heappop(heap)
    k = k - 1
print(-item)