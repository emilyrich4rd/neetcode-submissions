# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        else:
            out = []
            curr = head
            while curr != None:
                out.append(curr)
                curr = curr.next
            out[0] = ListNode(out[0].val, None)
            for i in range(1, len(out)):
                out[i] = ListNode(out[i].val, out[i-1])
            return out[-1]

       