# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        #we want to make sure the height of the left subtree and the height of the right subtree do not differ for more than one
        #i think we can definetly use DFS here to traverse the tree, and we can use a helper function to grab the height of each subtree


        def dfs(node):
            if not node:
                return True
            
            left = height(node.left)
            right = height(node.right)

            if abs(left - right) > 1:
                return False
            
            return dfs(node.left) and dfs(node.right)
            return True
        




        def height(node):
            if not node:
                return 0
            
            return 1 + max(height(node.left), height(node.right))

        
        return dfs(root)
        