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
        
        line = deque()
        line.append(root)

        process = []

        while line:
            size = len(line)

            for i in range(size):
                node = line.popleft()
                if node.left is not None:
                    line.append(node.left)
                if node.right is not None:
                    line.append(node.right)
                if i == size - 1:
                    process.append(node.val)
        

        return process