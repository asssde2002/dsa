from typing import List, Tuple
import heapq

def prim_algo(nodes: int, edges: List[Tuple[int, int, int]]):
    # TC: O((V+E)*log(V)), SC: O(V+E))
    node_edges = {i: [] for i in range(nodes)}
    for cost, v, u in edges:
        node_edges[v].append((cost, u))
        node_edges[u].append((cost, v))
    
    visited = [False] * nodes
    dp = [float("inf")] * nodes
    dp[0] = 0
    
    ans = 0
    pq = [(0, 0)]
    while pq:
        cost, node = heapq.heappop(pq)
        if visited[node]:
            continue
        
        visited[node] = True
        ans += cost
        for cost, vertex in node_edges[node]:
            if not visited[vertex]:
                heapq.heappush(pq, (cost, vertex))
                

    return ans if all(visited) else -1


if __name__ == "__main__":
    nodes = 6
    edges = [[16, 0, 1], [21, 0, 5], [19, 0, 4], [33, 4, 5], [18, 3, 4], [14, 3, 5],
             [11, 1, 5], [6, 1, 3], [5, 1, 2], [10, 2, 3]]
    mcst = prim_algo(nodes, edges)
    # 56
    print("Minimum Cost Spanning Tree: ", mcst)



