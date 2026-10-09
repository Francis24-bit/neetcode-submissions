# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        process = deque()
        process.append(root)
        final = []

        while process:
            size = len(process)
            for i in range(size):
                node = process.popleft()
                if node.left is not None:
                    process.append(node.left)
                if node.right is not None:
                    process.append(node.right)
                if i == size - 1:
                    final.append(node.val)
        
        return final