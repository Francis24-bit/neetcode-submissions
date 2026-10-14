# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indexBook = {}
        for index, value in enumerate(inorder):
            indexBook[value] = index

        rootIndex = 0
        def dfs(left, right):
            if right < left:
                return None
            nonlocal rootIndex
            #find root of the whole tree and make a TreeNode
            root = TreeNode(preorder[rootIndex])
            rootIndex += 1

            midIndex = indexBook[root.val]
            
            root.left = dfs(left, midIndex - 1)
            root.right = dfs(midIndex + 1, right)

            return root

        return dfs(0, len(inorder) - 1)