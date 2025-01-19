import heapq

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size    # optimize to make tree balanced

    def find(self, p):
        if p != self.parent[p]:
            self.parent[p] = self.find(self.parent[p])    # path compression

        return self.parent[p]

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)

        if root_p != root_q:
            if self.rank[root_p] > self.rank[root_q]:
                self.parent[root_q] = root_p
            elif self.rank[root_p] < self.rank[root_q]:
                self.parent[root_p] = root_q
            else:
                self.parent[root_q] = root_p
                self.rank[root_p] += 1


def kruskal_algo(nodes, edges):
    # TC: O(E*log(E)), SC: O(n)
    uf = UnionFind(nodes)
    heapq.heapify(edges)
    edges_count = 0
    costs = 0
    while edges_count < nodes-1 and edges:
        cost, v, u = heapq.heappop(edges)
        if uf.find(v) != uf.find(u):
            uf.union(u, v)
            edges_count += 1
            costs += cost
        
    return -1 if edges_count < nodes-1 else costs
    
