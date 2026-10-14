# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

    # Inorder: left, root, right, Preorder: root, left, right
    # Inorder: tell you the range,or what is to the left the root, what is right to the root
    # use preorde to find the root (first elemenet of the array)
    # use inorder to find leftree (left, midIndex - 1),
                        # righttree (midIndex + 1, right)
        indexBook = {}
        for index, value in enumerate(inorder):
            indexBook[value] = index

        node_pointer = 0
        def dfs(left, right):
            if right < left:
                return None
        
            nonlocal node_pointer
            #find root of the whole tree and make a TreeNode
            root = TreeNode(preorder[node_pointer])
            node_pointer += 1

            #find the positon of the root in inorder
            rootIndex = indexBook[root.val]
            
            root.left = dfs(left, rootIndex - 1)
            root.right = dfs(rootIndex + 1, right)

            return root

        return dfs(0, len(inorder) - 1)