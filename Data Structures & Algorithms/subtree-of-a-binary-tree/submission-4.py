# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


#we need to do validity checks, then run operation
#checks are seperate from operation.


        def sameTree(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            
            return sameTree(p.left,q.left) and sameTree(p.right,q.right)
        
        def dfs(tree, sub):
            if not sub or sameTree(tree, sub):
                return True

            if not tree:
                return False


            return dfs(tree.left, sub) or dfs(tree.right, sub)
        
        if not dfs(root, subRoot):
            return False
        
        return True
            
            
        