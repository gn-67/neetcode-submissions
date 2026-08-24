#we want to use a doubly linked list to maintain the leat used and most frequently used/added key

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        nxt = node.next
        prev = node.prev

        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        nxt = self.right
        prev = self.right.prev

        prev.next = node
        nxt.prev = node

        node.prev = prev
        node.next = nxt

        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        #we will use a hashmap storing nodes
        #we add it no matter what, then we check if cache is full
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
        else:
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            LRU = self.left.next
            del self.cache[LRU.key]
            self.remove(LRU)
        
    

