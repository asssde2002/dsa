def prim_algo(nodes, edges):
    # TC: O(V**2), SC: O(V+E)
    node_edges = {i: [] for i in range(nodes)}
    for cost, v, u in edges:
        node_edges[v].append((cost, u))
        node_edges[u].append((cost, v))
    
    collect_nodes = 1
    dp = [float("inf")] * nodes
    visited = [False] * nodes
    visited[0] = True
    for cost, u in node_edges[0]:
        dp[u] = min(dp[u], cost)

    ans = 0
    while collect_nodes != nodes:
        vertex = None
        min_cost = float("inf")
        for i in range(nodes):
            if not visited[i]:
                if dp[i] < min_cost:
                    vertex = i
                    min_cost = dp[i]

        if vertex is None:
            break

        visited[vertex] = True
        collect_nodes += 1
        ans += min_cost
        for cost, u in node_edges[vertex]:
            dp[u] = min(dp[u], cost)

    return ans if collect_nodes == nodes else -1


if __name__ == "__main__":
    nodes = 6
    edges = [[16, 0, 1], [21, 0, 5], [19, 0, 4], [33, 4, 5], [18, 3, 4], [14, 3, 5],
             [11, 1, 5], [6, 1, 3], [5, 1, 2], [10, 2, 3]]
    mcst = prim_algo(nodes, edges)
    # 56
    print("Minimum Cost Spanning Tree: ", mcst)


