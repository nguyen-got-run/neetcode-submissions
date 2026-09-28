class DoubleNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None
    
    def remove(self):
        prev, nxt = self.prev, self.next
        if prev: prev.next = nxt
        if nxt: nxt.prev = prev
    
    # link the current node with n1 and n2 (currently they're linking to each other)
    # result: n1 <-> n <-> n2
    def link(self, n1: DoubleNode, n2: DoubleNode):
        n1.next = self
        self.prev = n1

        n2.prev = self
        self.next = n2

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
    
        self.cache = {}
        # dummies (left - start, right - end of linked list)
        self.left, self.right = DoubleNode(), DoubleNode()
        # link dummies
        self.left.next = self.right
        self.right.prev = self.left
    
    # add a node to the end of the linked list
    def enqueue(self, node: DoubleNode):
        right = self.right
        last = right.prev

        node.link(last, right)

    # remove the first node of the linked list
    def dequeue(self):
        left = self.left
        n = left.next

        n.remove()

        return n.key

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # key in ht
        node = self.cache[key]

        node.remove()
        self.enqueue(node)

        return node.val
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].remove()
        
        node = DoubleNode(key, value)
        self.cache[key] = node
        self.enqueue(node)

        if len(self.cache) > self.capacity:
            k = self.dequeue()
            del self.cache[k]
