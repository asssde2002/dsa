from typing import List, Tuple
import heapq

# cannot have negative cost
# can have cycle
def dijkstra_algo(nodes: int, edges: List[Tuple[int, int, int]], source: int):
    # TC: O((V+E)*log(V)), SC: O(V+E))
    node_edges = {i: [] for i in range(nodes)}
    for cost, v, u in edges:
        node_edges[v].append((cost, u))
    
    distance = [float("inf")] * nodes
    distance[source] = 0

    pq = [(0, source)]
    while pq:
        curr_dist, node = heapq.heappop(pq)
        if curr_dist > distance[node]:
            continue
        
        for cost, vertex in node_edges[node]:
            if curr_dist + cost < distance[vertex]:
                dist = curr_dist + cost
                distance[vertex] = dist
                heapq.heappush(pq, (dist, vertex))
                

    return distance


if __name__ == "__main__":
    nodes = 8
    edges = [[250, 4, 5], [1500, 4, 3], [1000, 5, 3], [1400, 5, 7], [900, 5, 6],
             [1000, 6, 7], [1200, 3, 2], [800, 2, 1], [300, 1, 0], [1000, 2, 0], [1700, 7, 0]]
    source = 4
    distance = dijkstra_algo(nodes, edges, source)
    # [3350, 3250, 2450, 1250, 0, 250, 1150, 1650]
    print(distance)



