# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        #the diameter is the maximum between the left and the right subtrees
        self.diameter = 0

        def dfs(node):
            if not node:
                return 0
            
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)

            self.diameter = max(self.diameter, leftHeight + rightHeight)
            return 1 + max(dfs(node.left), dfs(node.right))




        dfs(root)
        return self.diameter

        