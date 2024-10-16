class Node:
    def __init__(self, data: int, lchild: "Node" = None, rchild: "Node" = None) -> None:
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


class BinaryTree:
    def traversal_preorder(self, root: "Node") -> None:
        if root is not None:
            print(root.data)                        # D
            self.traversal_preorder(root.lchild)    # L
            self.traversal_preorder(root.rchild)    # R

    def traversal_inorder(self, root: "Node") -> None:
        if root is not None:
            self.traversal_inorder(root.lchild)     # L
            print(root.data)                        # D
            self.traversal_inorder(root.rchild)     # R

    def traversal_postorder(self, root: "Node") -> None:
        if root is not None:
            self.traversal_postorder(root.lchild)   # L
            self.traversal_postorder(root.rchild)   # R
            print(root.data)                        # D
        
    def count_node(self, root: "Node") -> int:
        if root is None:
            return 0
        else:
            nl = self.count_node(root.lchild)
            nr = self.count_node(root.rchild)
            return nl + nr + 1
        
    def cal_height(self, root: "Node") -> int:
        if root is None:
            return 0
        else:
            lh = self.cal_height(root.lchild)
            rh = self.cal_height(root.rchild)
            return max(lh, rh) + 1
    
    def cal_leaf(self, root: "Node") -> int:
        if root is None:
            return 0
        else:
            nl = self.cal_leaf(root.lchild)
            nr = self.cal_leaf(root.rchild)
            if nl + nr == 0:
                return 1
            else:
                return nl + nr
    
    def copy(self, root: "Node") -> "Node":
        if root is None:
            return None
        else:
            new_root = Node()
            new_root.data = root.data
            new_root.lchild = self.copy(root.lchild)
            new_root.rchild = self.copy(root.rchild)
            return new_root
        
    def equal(self, root1: "Node", root2: "Node") -> bool:
        if root1 is None and root2 is None:
            return True
        elif root1 is not None and root2 is not None:
            if root1.data == root2.data:
                if self.equal(root1.lchild, root2.lchild) and self.equal(root1.rchild, root2.rchild):
                    return True
            else:
                return False
        else:
            return False

    def swap(self, root: "Node") -> None:
        if root is not None:
            self.swap(root.lchild)
            self.swap(root.rchild)
            root.lchild, root.rchild = root.rchild, root.lchild

        

def max_score(seq: list[int]) -> int:
    n = len(seq)
    def get_score(i: int) -> int:
        if i == n - 1:
            return 0
        
        score = 0
        for j in range(i+1, n):
            score = max(score, seq[j]*(j-i)+get_score(j))
        return score
    
    return get_score(0)