# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: 
            return True
        if not root:
            return False 
        
        #both trees are NOT empty

        if self.sameTree(root, subRoot):
            return True

        # ^ this is if they are the same tree

        return (self.isSubtree(root.right, subRoot)) or self.isSubtree(root.left, subRoot)
        # we add an OR because only one of the subtrees has to contain subtree


    
    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        
        if not root or not subRoot:
            return False
        
        if root.val != subRoot.val:
            return False

        return (self.sameTree(root.left, subRoot.left)) and (self.sameTree(root.right, subRoot.right))