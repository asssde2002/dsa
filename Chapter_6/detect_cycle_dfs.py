from typing import List


def get_safe_nodes_without_cycle(graph: List[List[int]]) -> List[int]:
    res = []
    n = len(graph)
    visit = [False] * n
    rec_stack = [False] * n
    for i in range(n):
        if not dfs(i, graph, visit, rec_stack):
            res.append(i)
            
    return res

def dfs(node, graph, visit, rec_stack):
    if rec_stack[node]:
        return True
    elif visit[node]:
        return False

    visit[node] = True
    rec_stack[node] = True
    for i in graph[node]:
        if dfs(i, graph, visit, rec_stack):
            return True
    
    rec_stack[node] = False
    return False


if __name__ == "__main__":
    graph = [[1,2],[2,3],[5],[0],[5],[],[]]
    # [2,4,5,6]
    print(get_safe_nodes_without_cycle(graph))

    graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
    # [4]
    print(get_safe_nodes_without_cycle(graph))
