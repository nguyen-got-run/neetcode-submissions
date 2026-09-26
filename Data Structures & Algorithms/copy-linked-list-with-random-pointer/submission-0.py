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
        # [[3,null],[7,3],[4,0],[5,1]]
        # [#null, #3, #0, #1]
        # [3, 7, 0, 1]

        old_to_new_map = {}
        cur = head

        while cur:
            old_to_new_map[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            new_1 = old_to_new_map[cur]
            new_1.next = old_to_new_map[cur.next] if cur.next else None
            new_1.random = old_to_new_map[cur.random] if cur.random else None

            cur = cur.next

        
        return old_to_new_map[head]


