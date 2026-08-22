# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # a node is good if it has not encountered a node greater than it on its path from root

        #we can use dfs here to traverse the binary tree
        #we can also use a result variable to keep track of our total good nodes
        #and to make sure our node isnt 'bad', we can use a maxVal to track the cur max


        def dfs (node, maxVal):
            if not node:
                return 0

            result = 0
            
            if node.val >= maxVal:
                result = 1
            
            maxVal = max(maxVal, node.val)
            
            #starting node is always valid
            result += dfs(node.left, maxVal) 
            result += dfs(node.right, maxVal)
            return result


        return dfs(root, -999)