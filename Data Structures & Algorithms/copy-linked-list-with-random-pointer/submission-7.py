"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head

        seen = {}

        cur = head
        while cur:
            nxt, val = cur.next, cur.val            
            seen[cur] = Node(val)
            cur = nxt
        
        cur = head
        while cur:
            nxt, rand = cur.next, cur.random
            node = seen[cur]

            if nxt: node.next = seen[nxt]
            if rand: node.random = seen[rand]

            cur = nxt

        return seen[head]
        

            


        