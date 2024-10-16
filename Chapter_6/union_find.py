# TC: O(1), SC: O(n)
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

    def get_components(self):
        for i in range(len(self.parent)):
            self.find(i)
        return set(self.parent)

