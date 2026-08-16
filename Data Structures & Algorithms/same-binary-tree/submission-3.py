# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(pSub, qSub):
            #if one exists but not the other, return false
            #if both don't exist, return false
            #if both exist AND both are equivalent, return true

            if not pSub and not qSub:
                return True
            if not pSub or not qSub:
                return False
            if pSub.val != qSub.val:
                return False

            return dfs(pSub.left, qSub.left) and dfs(pSub.right, qSub.right)
        
        return dfs(p,q)

        