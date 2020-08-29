times = [[2,1,1],[2,3,1],[3,4,1]]
N = 4
K = 2
# K是源点

# 堆实现
import collections
import heapq
graph = collections.defaultdict(list)
for u, v, w in times:
    graph[u].append((v, w))

# pq是小顶堆，其顶点是此时与源点最短距离的点的信息
pq = [(0, K)]
# 用于存储key到源点的最近距离（value）
dist = {}

while pq:
    d, node = heapq.heappop(pq)
    if node in dist:
        continue
    #     因为找到的点是越来越远，所以我们对同一个点，保存之前出现过的结果
    dist[node] = d
    for nei, d2 in graph[node]:
        if nei not in dist:
            heapq.heappush(pq, (d+d2, nei))
#             中间点node到源点是d nei到中间点是d2，所以d+d2

if len(dist) == N:
    print(max(dist.values()))
else:
    print(-1)

# 列表方法
def networkDelayTime(times, N, K):
    graph = collections.defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    # dist：key是图中顶点 value到源点的距离
    dist = {node: float('inf') for node in range(1, N + 1)}
    seen = [False] * (N + 1)
    # seen标记某个点是否已经走过
    dist[K] = 0
    # 源点距离为0
    while True:
        cand_node = -1
        cand_dist = float('inf')
        for i in range(1, N + 1):
            if not seen[i] and dist[i] < cand_dist:   # 如果未访问过，且到该店的距离小于之前的记录
                cand_dist = dist[i]   # 记录此时离源点最近的点的距离
                cand_node = i    # 记录此时离源点最近的点

        if cand_node < 0:
            break
        seen[cand_node] = True
        for nei, d in graph[cand_node]:
            dist[nei] = min(dist[nei], dist[cand_node] + d)   # 更新可以经过此时最近点到达的点距离源点的距离min（之前，源点到最近点+最近点到nei点）

    ans = max(dist.values())
    return ans if ans < float('inf') else -1
print(networkDelayTime(times, N, K))