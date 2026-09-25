"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# the idea is to map the old node to a new node, how ? by using a dictionary  copyMap[oldNode] = newNode

# do the loop 2 times, first time copy the node and the value
# second time, copy the oldNode.next and random.



class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyMap = {None : None}
        
        current = head
        while current != None:
            copyMap[current] = Node(current.val)
            current = current.next
        

        current = head
        while current != None:
            copy = copyMap[current]
            copy.next = copyMap[current.next]
            copy.random = copyMap[current.random]
            current = current.next
        
        return copyMap[head]