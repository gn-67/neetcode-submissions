# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if not node:
                return 0

            return 1 + max(height(node.left), height(node.right))
        
        def dfs(node):
            if not node:
                return 0
            
            return max(height(node.left) + height(node.right), dfs(node.left), dfs(node.right))
        
        return dfs(root)
        
        