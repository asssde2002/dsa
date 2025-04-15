# Binary Indexed Tree (Fenwick Tree) implementation
class BIT:
    def __init__(self, size):
        # start with 1-indexed array
        self.tree = [0] * (size+1)
    
    def update(self, index, delta):
        index += 1
        while index <= len(self.tree)-1:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        index += 1
        res = 0 
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        
        return res
    

if __name__ == "__main__":
    nums = [1, 3, 5, 7]
    bit = BIT(len(nums))
    for i, num in enumerate(nums):
        bit.update(i, num)
    
    sum_1_3 = bit.query(3) - bit.query(0)
    assert sum_1_3 == 15, f"Expected 15, got {sum_1_3}"