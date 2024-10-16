class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next


def invert_single_linked_list(node):
    r, q, p = None, None, node
    while p is not None:
        r = q
        q = p
        p = p.next
        q.next = r
    node = q
    return node


def get_node_data(node):
    data = []
    while node is not None:
        data.append(str(node.data))
        node = node.next
    
    return " -> ".join(data)


if __name__ == "__main__":
    end = Node(3)
    middle = Node(2, end)
    start = Node(1, middle)
    print("Original Linked List Data: ", get_node_data(start))
    print("Inverted Linked List Data: ", get_node_data(invert_single_linked_list(start)))
