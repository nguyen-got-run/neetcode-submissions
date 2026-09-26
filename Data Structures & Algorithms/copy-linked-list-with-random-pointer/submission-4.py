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

        cur = head
        head1 = Node(head.val)
        cur1 = head1
        oldPointerToNewNode = {}

        while cur:
            if cur not in oldPointerToNewNode:
                oldPointerToNewNode[cur] = cur1

            nxt, rand = cur.next, cur.random

            if nxt and nxt not in oldPointerToNewNode:
                node = Node(nxt.val)
                oldPointerToNewNode[nxt] = node
            
            if nxt:
                newNxt = oldPointerToNewNode[nxt]
                cur1.next = newNxt

            if rand and rand not in oldPointerToNewNode:
                node = Node(rand.val)
                oldPointerToNewNode[rand] = node
            
            if rand:
                newRand = oldPointerToNewNode[rand]
                cur1.random = newRand
            
            cur = nxt
            cur1 = newNxt if nxt else None
        
        return head1
        

            


        