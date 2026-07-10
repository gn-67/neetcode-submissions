# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #we can use recursive DFS to verify this is a BST
        #we can verify BST by using an upper and lower bound based on our root node, and updating it as we traverse down
        #lets use a helper function to track these parameters


        
        def valid(node, lower, upper):
            if not node:
                return True

            if not (node.val < upper and node.val > lower):
                return False
            

            return valid(node.left, lower, node.val) and valid(node.right, node.val, upper)

        return valid(root, -1001, 1001)