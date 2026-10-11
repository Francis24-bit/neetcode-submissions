# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
    # idea: low < val < high , for every node
    # if you go left, update the upper bound, keep low (as all nodes to the left must be smaller)
    # if you go right, update the lower bound, keep high (as all nodes to the right must be bigger)
        def bst(node, high, low):
            if node is None:
                return True
            
            if node.val >= high or node.val <= low:
                return False
            
            return bst(node.left, node.val,low) and bst(node.right, high, node.val)

        return bst(root, float('inf'), float('-inf'))