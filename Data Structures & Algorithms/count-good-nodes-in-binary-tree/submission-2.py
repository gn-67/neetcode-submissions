# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #we need to keep track of the count of good nodes
        #a good node is a node where no other node in its path from root are greater than that
        #that means every node we pass has to be greater than the max node value before it 
        #so we can track and update a max node in our dfs function
        #here I'll be using DFS as we want to explore each path to the end instead of focusing on our nodes neighbors



        def dfs(node, prevMax):
            if not node:
                return 0
            
            result = 0

            if node.val >= prevMax:
                result = 1
                prevMax = max(prevMax, node.val)
                
            
            result += dfs(node.left, prevMax)
            result += dfs(node.right, prevMax)


            return result 
        
        return dfs(root, -9999999)
        