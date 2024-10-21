class Node:
    def __init__(self, val=None, next_node=None):
        self.val = val
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def add_last_node(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next

            curr.next = node

    def add_first_node(self, val):
        node = Node(val, self.head)
        self.head = node
    
    def remove_last_node(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head = None
            return

        curr = self.head
        while curr and curr.next and curr.next.next:
            curr = curr.next

        curr.next = None

    def remove_first_node(self):
        if self.head is None:
            return
        else:
            self.head = self.head.next

    def __str__(self):
        curr = self.head
        res = []
        while curr:
            res.append(str(curr.val))
            curr = curr.next
        
        return ", ".join(res)

if __name__ == "__main__":
    ll = LinkedList()
    ll.add_last_node(10)
    ll.add_last_node(-5)
    ll.add_last_node(9)
    print(ll)
    ll.add_first_node(8)
    print(ll)
    ll.remove_last_node()
    print(ll)
    ll.remove_first_node()
    print(ll)
