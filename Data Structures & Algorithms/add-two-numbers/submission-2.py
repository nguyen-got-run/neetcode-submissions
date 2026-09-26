# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = 0, 0
        i1, i2 = 0, 0

        cur1 = l1
        while cur1:
            val, nxt = cur1.val, cur1.next
            i1 += 10**n1 * val
            n1 += 1

            cur1 = nxt

        cur2 = l2
        while cur2:
            val, nxt = cur2.val, cur2.next
            i2 += 10**n2 * val 
            n2 += 1

            cur2 = nxt
        
        total = str(i1 + i2)
        prev = None

        for i in range(len(total)):
            val = int(total[i])
            node = ListNode(val)
            node.next = prev

            prev = node
        
        return prev





        