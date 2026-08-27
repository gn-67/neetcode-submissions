# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return 
            
            temp = node.left
            node.left = node.right
            node.right = temp
            dfs(node.left)
            dfs(node.right)
            return 
        
        dfs(root)
        return root




        #clarifying question
        #we can brainstorm an implementation together, maybe run it through a simple test caes
        #code it up
        #analyze time space complexity
        #verify code by running through test cases + edge cases
        