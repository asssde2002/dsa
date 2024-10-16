def prime_algo(nodes, edges):
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


