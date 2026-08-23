# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        #the maximum between the height of the left subtree and the right subtree
        #so what I'll do is create a helper function to calculate hegiht of a tree at the node and then use DFS to return the max height between left subtree and right subtree


        def height(node):
            if not node:
                return 0
            
            return 1 + max(height(node.left),height(node.right))
        
        def dfs(node):
            if not node:
                return 0
            
            return max(height(node.left) + height(node.right), dfs(node.left), dfs(node.right))
        
        return dfs(root)