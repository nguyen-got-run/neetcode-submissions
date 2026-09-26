# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: return None

        slow, fast = head, head.next

        while fast and fast.next:
            if slow is fast: return None
            slow = slow.next
            fast = fast.next.next
        
        # at this point, we've done 2 things:
        # 1) detect if there's a cycle -> then return None
        # 2) split the list in half, with slow being the last node of the first half
        #    and fast being the first node of the second half
        # now we need to reverse the 2nd half

        sec = slow.next
        # disconnect first with second half
        slow.next = None

        prev = None
        # reverse the 2nd part:
        while sec:
            nxt = sec.next
            sec.next = prev

            prev = sec
            sec = nxt
        
        # merge
        fst, sec = head, prev

        while sec:
            nxt1 = fst.next
            sec1 = sec.next

            fst.next = sec
            sec.next = nxt1

            fst = nxt1
            sec = sec1




        
        