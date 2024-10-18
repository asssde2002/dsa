from typing import List, Tuple

# cannot have negative cycle
# can have negative cost
def bellman_ford(nodes: int, edges: List[Tuple[int, int, int]], source: int):
    # TC: O(V*E), SC: O(V+E)
    distance = [float("inf")] * nodes
    distance[source] = 0
    # relaxing
    for _ in range(nodes-1):
        for cost, v, u in edges:
            if distance[v] != float("inf") and distance[v]+cost < distance[u]:
                distance[u] = distance[v] + cost

    # check negative cycle
    for cost, v, u in edges:
        if distance[v] != float("inf") and distance[v]+cost < distance[u]:
            return None

    return distance


if __name__ == "__main__":
    nodes = 7
    edges = [[6, 0, 1], [5, 0, 2], [-2, 2, 1], [5, 0, 3], [-1, 3, 5], [-2, 3, 2], 
             [1, 2, 4], [-1, 1, 4], [3, 4, 6], [3, 5, 6]]
    source = 0
    distance = bellman_ford(nodes, edges, source)
    if distance is not None:
        # [0, 1, 3, 5, 0, 4, 3]
        print(distance)
    else:
        print("detect negative cycle")

    edges = [[-4, 1, 0], [5, 0, 2], [-2, 2, 1], [5, 0, 3], [-1, 3, 5], [-2, 3, 2], 
             [1, 2, 4], [-1, 1, 4], [3, 4, 6], [3, 5, 6]]
    distance = bellman_ford(nodes, edges, source)
    if distance is not None:
        print(distance)
    else:
        print("detect negative cycle")
