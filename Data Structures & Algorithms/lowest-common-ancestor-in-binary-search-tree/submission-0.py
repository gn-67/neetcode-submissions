# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        #cur will never be null, this is just to get the code to execute
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
                #search the right subtree            
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
                #search the left subtree

            else:
                return cur
            
        
        