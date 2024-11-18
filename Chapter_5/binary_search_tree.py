class Node:
    def __init__(self, val, lchild=None, rchild=None):
        self.val = val
        self.lchild = lchild
        self.rchild = rchild

class BinarySearchTree:
    def search(self, node, k: int) -> bool:
        if node is None:
            return False
        else:
            if node.val > k:
                return self.search(node.lchild, k)
            elif node.val < k:
                return self.search(node.rchild, k)
            else:
                return True
        
