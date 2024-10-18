from typing import List
from copy import deepcopy

# can have negative cost
# can not have negative cycle
def floyd_warshall(graph: List[List[int]]):
    # TC: O(V**3), SC: O(V**2)
    nodes = len(graph)
    distance = deepcopy(graph)

    for k in range(nodes):
        for i in range(nodes):
            for j in range(nodes):
                distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])

    for i in range(nodes):
        for j in range(nodes):
            if distance[i][j] < 0:
                return None

    return distance



if __name__ == "__main__":
    INF = float('inf')
    graph = [
        [0, 5, INF, 10],
        [INF, 0, 3, INF],
        [INF, INF, 0, 1],
        [INF, INF, INF, 0]
    ]

    distance = floyd_warshall(graph)
    
    print("Shortest distances between every pair of vertices:")
    for node, row in enumerate(distance):
        print(f"Node({node}): ", row)
