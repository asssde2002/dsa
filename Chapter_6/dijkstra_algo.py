from typing import List

# cannot have negative cost
def dijkstra_algo(nodes: int, edges: List[List[int]], source: int):
    # TC: O(V**2), SC: O(V+E))
    node_edges = {i: [] for i in range(nodes)}
    for cost, v, u in edges:
        node_edges[v].append((cost, u))
    
    collect_nodes = 0
    distance = [float("inf")] * nodes
    visited = [False] * nodes
    distance[source] = 0

    while collect_nodes != nodes:
        vertex = None
        min_cost = float("inf")
        for i in range(nodes):
            if not visited[i]:
                if distance[i] < min_cost:
                    vertex = i
                    min_cost = distance[i]

        if vertex is None:
            break

        visited[vertex] = True
        collect_nodes += 1
        for cost, u in node_edges[vertex]:
            if not visited[u]:
                distance[u] = min(distance[u], distance[vertex]+cost)

    return distance


if __name__ == "__main__":
    nodes = 8
    edges = [[250, 4, 5], [1500, 4, 3], [1000, 5, 3], [1400, 5, 7], [900, 5, 6],
             [1000, 6, 7], [1200, 3, 2], [800, 2, 1], [300, 1, 0], [1000, 2, 0], [1700, 7, 0]]
    source = 4
    distance = dijkstra_algo(nodes, edges, source)
    # [3350, 3250, 2450, 1250, 0, 250, 1150, 1650]
    print(distance)


