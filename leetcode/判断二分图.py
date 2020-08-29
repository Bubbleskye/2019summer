# 如果给定的无向图连通，那么我们就可以任选一个节点开始，给它染成color=0。
# 随后我们对整个图进行遍历，将该节点直接相连的所有节点染成1-color，表示这些节点不能与起始节点属于同一个集合。
# 我们再将这些1-color节点直接相连的所有节点染成color，以此类推，直到无向图中的每个节点均被染色。
# 如果我们能够成功染色，那么0和1的节点各属于一个集合，这个无向图就是一个二分图；
# 如果我们未能成功染色，即在染色的过程中，某一时刻访问到了一个已经染色的节点，
# 并且它的颜色与我们将要给它染上的颜色不相同，也就说明这个无向图不是一个二分图。
def isBipartite(graph):
    '''
    深度优先遍历（DFS）
    利用染色法，遍历所有的节点，相邻的节点为不同的颜色
    如果相邻的节点染色为相同的颜色，那么直接返回False
    当所有点着色完毕，并且没有相邻节点相同的颜色，那么返回True
    '''
    visited = [False] * len(graph)  ## 标识节点是否被访问过
    colors = [-1] * len(graph)  ## 第i个节点着色为0或者1，-1表示未着色

    def helper(node, color, colors, visited):
        '''
        从节点node开始，遍历整个联通图， node表示开始的节点， color表示这个节点着色为color
        '''
        visited[node] = True
        colors[node] = color
        ## dfs遍历整个联通图
        for n in graph[node]:
            if not visited[n]:
                if not helper(n, 1 - color, colors, visited):
                    return False
            else:
                if colors[n] == color:
                    return False
                else:
                    continue
        return True

    ## 遍历所有连通图
    for i in range(len(graph)):
        if not visited[i]:
            if not helper(i, 0, colors, visited):
                return False
        else:
            continue
    return True

graph=[[1,2,3], [0,2], [0,1,3], [0,2]]
print(isBipartite(graph))