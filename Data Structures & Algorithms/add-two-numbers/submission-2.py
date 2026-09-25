# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # get the value of each position, if none, then value = 0
        # set up a carry, use % for oneth postion and // for tenth position, the carry
        # move the 2 pointers

        p1 = l1
        p2 = l2

        carry = 0
        dummy = ListNode()
        current = dummy

        while p1 != None or p2 != None or carry != 0:
            if p1 != None:
                value1 = p1.val
            else:
                value1 = 0
            
            if p2 != None:
                value2 = p2.val
            else:
                value2 = 0
            
            total = value1 + value2 + carry
            onePosition = total % 10
            carry = total // 10

            current.next = ListNode(onePosition)
            current = current.next

            if p1 != None:
                p1 = p1.next
            if p2 != None:
                p2 = p2.next
        
        return dummy.next
    
            