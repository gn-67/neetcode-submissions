# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:


        #BST means values on the left are smaller than root
        # values on the right GREATER than root
        # a node CAN be a descendant of itself

        
        #if both nodes are less than the root node
        #root = root.left
        #if both nodes are greater than the root node
        #root = root.right
        
        def dfs(node):


            if (p.val <= node.val and q.val >= node.val) or (q.val <= node.val and p.val >= node.val):
                return node
            
            if p.val < node.val and q.val < node.val:
                return dfs(node.left)
            
            return dfs(node.right)
        
        return dfs(root)