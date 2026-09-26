# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return head

        # check if there's a loop
        slow, fast = head, head.next

        while fast and fast.next:
            if slow is fast: return head

            slow = slow.next
            fast = fast.next.next
        
        # exited -> no loop
        # reverse the list
        prev, cur = None, head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        # reverse again, and remove the nth from the start
        cur = prev
        prev = None
        count = 1

        while cur:
            nxt = cur.next
            if count != n:
                cur.next = prev
                prev = cur
            cur = nxt
            count += 1
        
        return prev
