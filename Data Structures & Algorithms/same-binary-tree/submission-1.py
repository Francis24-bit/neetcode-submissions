# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        
        elif p == None or q == None:
            return False
        
        elif p.val == q.val:
            left_result = self.isSameTree(p.left, q.left)
            right_result = self.isSameTree(p.right, q.right)
        
        else:
            return False

        if left_result == True and right_result == True:
            return True

        return False