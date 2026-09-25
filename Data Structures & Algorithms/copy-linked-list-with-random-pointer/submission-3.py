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

# step 1: use a dictionary {oldNode : [Node] +Value}

# step 2: loop the old linked-list, get the [Node], and connect them as the old linked-list way
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