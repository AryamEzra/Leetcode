# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.arr = []
        if not root:
            return None
        
        def dfs(node, cur):
            if not node:
                return None

            cur = (cur << 1) | node.val
            if not node.left and not node.right:
                self.arr.append(cur)
                return
            
            dfs(node.left, cur)
            dfs(node.right, cur)

        
        dfs(root, 0)
        return sum(self.arr)       