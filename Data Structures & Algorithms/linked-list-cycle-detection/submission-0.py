# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = {}
        curr = head
        while curr != None:
            if nodes.get(curr.val) == None:
                nodes[curr.val] = [curr]
            else:
                if curr in nodes[curr.val]:
                    return True
                else:
                    nodes[curr.val].append(curr)
            curr = curr.next
        return False