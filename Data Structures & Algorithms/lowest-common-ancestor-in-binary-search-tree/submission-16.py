# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #all nodes to the left need to be smalle rthant the root
        #and all nodes to the right need to be greater than the root

        #so if our two node values are split among the root, we know that the root has to be the LCA
        #otherwise if both nodes are greater, we have to search right on our treee, and left otherwise
        #we can traverse our tree using DFS


        def dfs(node):

            if p.val < node.val and q.val < node.val:
                return dfs(node.left)
            if p.val > node.val and q.val > node.val:
                return dfs(node.right)


            return node

        
        return dfs(root)
            
            