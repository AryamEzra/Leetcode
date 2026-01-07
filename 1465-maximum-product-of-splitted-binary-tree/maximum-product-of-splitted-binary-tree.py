# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        def dfs_total(node):
            if not node:
                return 0
            return node.val + dfs_total(node.left) + dfs_total(node.right)
        
        self.total = dfs_total(root)

        self.ans = 0
        def dfs_subtree(node):
            if not node:
                return 0
            l = dfs_subtree(node.left)
            r = dfs_subtree(node.right)

            self.ans = max(self.ans, (self.total - l ) * l, (self.total - r) * r )

            return node.val + l + r
        dfs_subtree(root)
        return self.ans % (10 ** 9 + 7)