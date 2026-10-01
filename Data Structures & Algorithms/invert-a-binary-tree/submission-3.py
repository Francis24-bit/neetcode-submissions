# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

# Use deque so that popleft() is fast. With a list, pop(0) removes the first element,
# so all following elements need to shift positions.
# Idea: the deque stores all nodes that still need to be handled.
# While the queue is not empty, take out the first node and swap its left and right children.
# If the left and/or right child is not None, add it to the queue to be handled later.
        if not root:
            return None
        queue = deque([root])
        while queue:
            node = queue.popleft()
            temp = node.left
            node.left = node.right
            node.right = temp
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        
        return root