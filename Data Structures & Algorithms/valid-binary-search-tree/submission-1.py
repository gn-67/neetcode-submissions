# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        # we can use recursive DFS to verify the tree
        # since we know the left subtree always has to be less than the root, right subtree greater
        # we can do DFS while maintaining a valid range of values, any violation will return in us returning false


        def valid (node, upper, lower):
            if not node:
                return True #we passed through every node without failing
            
            if not (lower < node.val and upper > node.val):
                return False

            return valid(node.left, node.val, lower) and valid(node.right, upper, node.val,)
        
        return valid(root, 1001, -1001)
        