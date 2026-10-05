# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
# 1. Check base cases first:
#    - both None -> True
#    - only one None -> False
# 2. Then two cases:
#    Case 1: they start at the same node (root, subRoot) -> check isSameTree(root, subRoot)
#    Case 2: they don't start at the same node -> check isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)
        if root is None and subRoot is None:
            return True
        elif root is None or subRoot is None:
            return False
        elif self.isSameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

    def isSameTree(self, root, subRoot):
        if root is None and subRoot is None:
            return True
        elif root is None or subRoot is None:
            return False
        elif root.val != subRoot.val:
            return False
        else:
            return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)