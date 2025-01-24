from collections import deque
from typing import List

def get_safe_nodes_without_cycle(graph: List[List[int]]) -> List[int]:
    n = len(graph)
    adj = [[] for _ in range(n)]
    in_degree = {i: 0 for i in range(n)}
    for i in range(n):
        for j in graph[i]:
            adj[j].append(i)
            in_degree[i] += 1

    q = deque()
    for i in range(n):
        if in_degree[i] == 0:
            q.append(i)
    
    safe = [False] * n
    while q:
        node = q.popleft()
        safe[node] = True
        for nei in adj[node]:
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                q.append(nei)
    
    res = []
    for i in range(n):
        if safe[i]:
            res.append(i)
    
    return res

if __name__ == "__main__":
    graph = [[1,2],[2,3],[5],[0],[5],[],[]]
    # [2,4,5,6]
    print(get_safe_nodes_without_cycle(graph))

    graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
    # [4]
    print(get_safe_nodes_without_cycle(graph))
