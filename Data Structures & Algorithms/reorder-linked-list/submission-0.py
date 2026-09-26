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
            next1 = cur.next

            # update pointer
            cur.next = prev

            #update cur
            prev = cur
            cur = next1
        
        return prev

    def splitListHalf(self, head: Optional[ListNode]) -> tuple[head: Optional[ListNode], head: Optional[ListNode]]:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_head = slow.next
        slow.next = None
        return head, second_head

    def reorderList(self, head: Optional[ListNode]) -> None:
        first, second = self.splitListHalf(head)

        second = self.reverseList(second)

        while second:
            temp1, temp2 = first.next, second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
        