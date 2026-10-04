# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
# both None -> True
# only one None -> False
# values equal -> check left and right subtrees
#   (use `and` so if left is False, right is never checked, saving cost)
# values differ -> False
        if p is None and q is None:
            return True
        
        elif p is None or q is None:
            return False
        
        elif p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        else:
            return False