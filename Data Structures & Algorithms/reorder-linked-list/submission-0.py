# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # if you want the left-mid, start with fast.head.next
        slow = head
        fast = head.next

    #as you need to make the move (fast = fast.next.next)
    # to do that, fast has to be valid, and fast.next has to be valid as well.
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        new_start = slow.next # find the start of the 2nd half
        slow.next = None #cut the first half

        previous = None
        current = new_start
        while current:
            next_node = current.next
            current.next = previous

            previous = current
            current = next_node
        # what is the head of the reversed linked-list：previous
        while previous:
            new_node1 = head.next
            new_node2 = previous.next

            head.next = previous
            previous.next = new_node1

            head = new_node1
            previous = new_node2