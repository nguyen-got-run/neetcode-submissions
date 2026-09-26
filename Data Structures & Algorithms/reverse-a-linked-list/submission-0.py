# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            the_next = cur.next

            # point to prev
            cur.next = prev

            # update
            prev = cur
            cur = the_next

        return prev
        