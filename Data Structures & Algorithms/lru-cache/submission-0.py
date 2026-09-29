class LRUCache:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.book = {}
        self.left = self.Node(0, 0)
        self.right = self.Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        prev = self.right.prev
        node.prev = prev
        node.next = self.right
        prev.next = node
        self.right.prev = node

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key not in self.book:
            return -1
        node = self.book[key]
        self.remove(node)
        self.insert(node)
        return node.value
        
    def put(self, key: int, value: int) -> None:
        if key in self.book:
            node = self.book[key]
            node.value = value
            self.remove(node)
            self.insert(node)
        else:
            node = self.Node(key, value)
            self.book[key] = node
            self.insert(node)
            if len(self.book) > self.capacity:
                node = self.left.next
                self.remove(node)
                del self.book[node.key]