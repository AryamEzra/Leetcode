# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None

        max_val = float('-inf')
        ans_lvl = 0

        queue = deque()
        queue.append(root)
        
        cur_lvl = 0
        while queue:
            level = 0
            cur_lvl += 1
            n = len(queue)

            for i in range(n):
                node = queue.popleft()
                level += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            if level > max_val:
                max_val = max(max_val, level)
                ans_lvl = cur_lvl

        return ans_lvl

            
        

        