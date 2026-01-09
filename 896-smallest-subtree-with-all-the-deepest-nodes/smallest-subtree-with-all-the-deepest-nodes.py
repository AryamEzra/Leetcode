# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node): # node, depth
            if not node:
                return (None, 0)
            left_node, ld = dfs(node.left)
            right_node, rd = dfs(node.right)

            if ld > rd:
                return (left_node, ld + 1)
            elif rd > ld:
                return (right_node, rd + 1)
            else:
                return (node, ld + 1)

        return dfs(root)[0]