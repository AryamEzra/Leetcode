# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []

    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.inorderTraversal(root)
        return self.sortedArrayToBST(self.ans)
    
    def inorderTraversal(self, root: TreeNode) -> None:
        if root:
            self.inorderTraversal(root.left)
            self.ans.append(root.val)
            self.inorderTraversal(root.right)
    
    def sortedArrayToBST(self, arr) -> TreeNode:
        if not arr:
            return None
        
        mid = len(arr) // 2
        root = TreeNode(arr[mid])
        root.left = self.sortedArrayToBST(arr[:mid])
        root.right = self.sortedArrayToBST(arr[mid+1:])
        return root