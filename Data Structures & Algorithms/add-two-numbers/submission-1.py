# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        carry = 0 
        while curr1 and curr2:
            sum = curr1.val + curr2.val + carry
            print(sum)
            if sum > 9:
                carry = sum // 10
            else:
                carry = 0 
            curr1.val = sum % 10
            curr2.val = sum % 10
            nextCheck = curr1.next or curr2.next
            if not nextCheck and carry > 0:
                curr1.next = ListNode(carry, None)
                return l1
            curr1 = curr1.next
            curr2 = curr2.next

        nonNull = curr1 if curr1 else curr2
        head = l1 if curr1 else l2

        while nonNull:
            sum = nonNull.val + carry
            if sum > 9:
                carry = sum // 10
            else:
                carry = 0 
            nonNull.val = sum % 10
            if not nonNull.next and carry > 0:
                nonNull.next = ListNode(carry, None)
                return head
            nonNull = nonNull.next
        return head
            
