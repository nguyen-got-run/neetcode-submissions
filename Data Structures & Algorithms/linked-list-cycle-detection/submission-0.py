# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head

        while fast and fast.next:
            head = head.next
            fast = fast.next.next

            if head is fast:
                return True
        
        return False
        