# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def helper(left, right):
            if not left and not right:
                return True

            if not left or not right:
                return False
            
            if left.val != right.val:
                return False
            
            return helper(left.left, right.left) and helper(left.right, right.right)
        

        def dfs(tree, subTree):
            if not subTree or helper(tree, subTree):
                return True
            
            if not tree:
                return False


            
            return dfs(tree.left, subTree) or dfs(tree.right, subTree)

        
        return dfs(root, subRoot)
            