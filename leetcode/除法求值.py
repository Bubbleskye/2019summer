equations=[["a","b"],["b","c"]]
values=[2.0,3.0]
queries=[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
graph = {}
for (x, y), v in zip(equations, values):
# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
    if x in graph:
        graph[x][y] = v
    else:
        graph[x] = {y: v}
    if y in graph:
        graph[y][x] = 1 / v
    else:
        graph[y] = {x: 1 / v}
# 字典嵌套
# graph={'a': {'b': 2.0}, 'b': {'a': 0.5, 'c': 3.0}, 'c': {'b': 0.3333333333333333}}
# dfs找寻从s到t的路径并返回结果叠乘后的边权重即结果
def dfs(s, t) -> int:
    if s not in graph:
        return -1
    if t == s:
        return 1
    for node in graph[s].keys():
        # 查到值时
        if node == t:
            return graph[s][node]
        elif node not in visited:
            visited.add(node)  # 添加到已访问避免重复遍历
            v = dfs(node, t)
            if v != -1:
                return graph[s][node] * v
    return -1


# 逐个计算query的值
res = []
for qs, qt in queries:
    visited = set()
    res.append(dfs(qs, qt))
print(res)