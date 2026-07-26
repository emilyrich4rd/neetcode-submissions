# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0 
        curr = head
        while curr:
            curr = curr.next
            count += 1
        k = count + 1 - n 

        if k == 1:
            return head.next 

        count = 0 
        curr = head
        prev = None      
        while curr:
            count += 1
            if count == k:
                prev.next = curr.next
                return head

            prev = curr
            curr = curr.next
        return head