# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def toNum(self, li: Optional[ListNode]) -> int:
        numeric = ''
        cur = li
        while cur:
            numeric += str(cur.val)
            cur = cur.next
        
        return int(numeric[::-1])

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2: return null

        num1 = self.toNum(l1)
        num2 = self.toNum(l2)
        total = num1 + num2

        prev = None
        cur = None

        for ch in str(total):
            cur = ListNode(int(ch))
            cur.next = prev

            prev = cur
        
        return cur