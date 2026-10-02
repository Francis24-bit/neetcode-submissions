# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.diameter = 0
    
        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
                
            step = left + right
            self.diameter = max(self.diameter, step)

            max_depth = max(left, right) + 1
            return max_depth
        
        depth(root)

        return self.diameter