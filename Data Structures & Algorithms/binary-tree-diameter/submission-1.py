# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    # the idea is to update the longest path (the left_depth + the right_depth) at each node, and node_depth is decided by the max of (left and right) depth. + 1
        self.diameter = 0

        def depth(node):
            if not node:
                return 0
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            node_depth = max(left_depth, right_depth) + 1

            distance = left_depth + right_depth
            self.diameter = max(self.diameter, distance)
            return node_depth

        depth(root)

        return self.diameter