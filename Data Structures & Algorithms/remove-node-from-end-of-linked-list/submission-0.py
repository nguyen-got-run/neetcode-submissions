# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total = 0
        cur = head

        while cur:
            total += 1
            cur = cur.next
        
        if total == n:
            return head.next

        i = 0
        i_toremove = total - n
        prev = None
        cur = head
        while cur:
            next1 = cur.next

            if i == i_toremove:
                prev.next = next1
            
            else:
                prev = cur
            
            cur = next1
            i += 1
        
        return head

