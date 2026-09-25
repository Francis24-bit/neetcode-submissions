"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

# step 1: use a dictionary to copy the old node with a new Node along with the value

# step 2: loop the old list, and get the values of the dictionary along the way, and conncet them
        copyMap = {None : None}

        current = head
        while current != None:
            copyMap[current] = Node(current.val)
            current = current.next
        
        current = head
        while current != None:
            copyNode = copyMap[current]
            copyNode.next = copyMap[current.next]
            copyNode.random = copyMap[current.random]
            current = current.next
        
        return copyMap[head]