# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
# Use a deque for FIFO processing, and a final [] for the result

# Put root in the deque. For each level:
#   - level_size = len(deque) -> number of pops for THIS level
#   - pop each node, add node.val to this level's list
#   - push its left and right children into the deque (for the next level)
# Append this level's list to final

        line = deque()
        final = []

        if root is None:
            return []
        line.append(root)

        while line:
            level_size = len(line)
            level_list = []
            for _ in range(level_size):
                node = line.popleft()
                level_list.append(node.val)
                if node.left is not None:
                    line.append(node.left)
                if node.right is not None:
                    line.append(node.right)
            final.append(level_list)

        return final
