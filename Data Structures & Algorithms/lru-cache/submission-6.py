class DoubleNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None
    
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
    
        self.ht = {}
        self.left, self.right = DoubleNode(), DoubleNode()
        self.left.next = self.right
        self.right.prev = self.left
    
    def insert_left(self, node: DoubleNode):
        node.next = self.left.next
        self.left.next.prev = node

        self.left.next = node
        node.prev = self.left

    def remove_self(self, node: DoubleNode):
        prev, next = node.prev, node.next

        # connect prev & next
        if prev: prev.next = next
        if next: next.prev = prev


    def get(self, key: int) -> int:
        if key not in self.ht:
            return -1
        
        node = self.ht[key]

        # detach & append to first of list
        self.remove_self(node)
        self.insert_left(node)

        return node.val
    
    def put(self, key: int, value: int) -> None:
        if key in self.ht:
            self.remove_self(self.ht[key])
        
        node = DoubleNode(key, value)
        self.ht[key] = node
        self.insert_left(node)

        if len(self.ht) > self.capacity:
            toremove_node = self.right.prev
            self.remove_self(toremove_node)
            del self.ht[toremove_node.key]
        

        


