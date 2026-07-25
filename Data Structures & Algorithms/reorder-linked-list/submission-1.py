# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first get head of the second half by finding when fast = None, then taking slow
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        mid = slow
        next = slow.next
        mid.next = None
        # now reverse second half of the list
        while next:
            old_next = next.next
            next.next = mid 
            mid = next
            next = old_next
        l1 = head
        l2 = mid
        while l2.next:
            l1_next, l2_next = l1.next, l2.next
            l1.next = l2
            l2.next = l1_next
            l1 = l1_next
            l2 = l2_next
        l1.next = l2
        l2.next = None
