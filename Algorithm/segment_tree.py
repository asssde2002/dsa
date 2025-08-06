from typing import List

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = 1 << (self.n-1).bit_length()
        self.tree = [0] * (2*self.size)

        for i in range(self.n):
            self.tree[self.size + i] = data[i]

        for i in range(self.size-1, 0, -1):
            self.tree[i] = max(self.tree[2*i], self.tree[2*i+1])

    def update(self, index, value):
        pos = self.size + index
        self.tree[pos] = value
        while pos > 1:
            pos >>= 1
            self.tree[pos] = max(self.tree[2*pos], self.tree[2*pos+1])
    
    def find(self, val):
        if self.tree[1] < val:
            return False
        
        idx = 1
        while idx < self.size:
            if self.tree[2*idx] >= val:
                idx = 2 * idx
            else:
                idx = 2 * idx + 1
        
        actual_idx = idx - self.size
        self.update(actual_idx, 0)
        return True

if __name__ == "__main__":
    # leetcode 3479
    def numOfUnplacedFruits(fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits) 

        tree = SegmentTree(baskets)
        res = 0
        for i in range(n):
            if tree.find(fruits[i]) is False:
                res += 1
        
        return res


    # Example usage
    fruits = [4, 2, 5]
    baskets = [3, 5, 4]
    unset = numOfUnplacedFruits(fruits, baskets)
    print("Number of unplaced fruits:", unset)  # 1

    fruits = [3, 6, 1]
    baskets = [6, 4, 7]
    unset = numOfUnplacedFruits(fruits, baskets)
    print("Number of unplaced fruits:", unset)  # 0

