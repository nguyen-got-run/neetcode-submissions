# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1
        if not list1 and not list2: return list1

        head = ListNode
        cur = head

        # we are changing ref for list1 and list2
        # once one of the list reaches the end, we can stop there
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            
            cur = cur.next

        # since we soop when list1 ends or when list2 ends
        # we have to bind cur.next to rest of the other
        cur.next = list1 or list2

        return head.next
