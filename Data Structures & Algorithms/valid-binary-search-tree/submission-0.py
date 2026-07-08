# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #we can use DFS here, lets write a recursive helper function

        def valid (node, left, right):
            if not node: #we reach an empty node, we return true,m technically empty tree is valid 
                return True #im having trouble  determining the base case, how do we just know to create a herlper function and why is it usually this and sometimes its other conditions as base case? is it basically the opposite of the False condition, so like if the false condition isn't hit, then that means we clear to run this which is true

            if not (node.val < right and node.val > left):
                return False
                # we found a node that breaks thie "rule"
            #every value in the left subtree has to be less than the parent
            return (valid(node.left, left, node.val) and valid(node.right, node.val, right)) #we check the right side as well
            
        return valid (root, -1001, 1001)

        