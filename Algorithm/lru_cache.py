class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    # TC: O(1), SC: O(n)
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self._remove(node)
            self._add(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            node.val = value
            self._remove(node)
            self._add(node)
        else:
            new_node = ListNode(key, value)
            if len(self.dict) >= self.capacity:
                old_node = self.head.next
                self._remove(old_node)
                del self.dict[old_node.key]

            self._add(new_node)
            self.dict[key] = new_node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail

    def __str__(self):
        curr = self.head.next
        res = []
        while curr != self.tail:
            res.append(f"{curr.key}-{curr.val}")
            curr = curr.next

        return ", ".join(res)
        

if __name__ == "__main__":
    cache = LRUCache(3)
    cache.put("a", 1)
    cache.put("b", 2)
    print("After put key 'b', Cache content:", cache)
    print("Cache get key 'a':", cache.get("a"))
    print("After get key 'a', Cache content:", cache)
    cache.put("a", 3)
    print("After put key 'a', Cache content:", cache)
    cache.put("c", 4)
    print("After put key 'c', Cache content:", cache)
    cache.put("d", 5)
    print("After put key 'd', Cache content:", cache)

