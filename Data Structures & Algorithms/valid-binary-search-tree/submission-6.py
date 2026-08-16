# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#wait
#the proper way to implement this is to keep track of a min and a max
#and run dfs using the current node as the max and such

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def dfs(node, minimum, maximum):
            if not node:
                return True

            if node.val >= maximum or node.val <= minimum:
                return False
            
            return dfs(node.left, minimum, node.val) and dfs(node.right, node.val, maximum)
        

        return dfs(root, -1000000001, 1000000000)
        