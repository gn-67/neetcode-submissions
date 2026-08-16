# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        #we can use BFS here for level order traversal
        #add the first node to the queue
        #while the q exists, we pop first value
        #add it to the level
        #add nodes neighbors to the queue
        #add the level to the result
        result = []

        def bfs(tree):
            q = collections.deque()
            q.append(root)

            while q:
                length = len(q)
                level = []
                for i in range(length):
                    node = q.popleft()
                    if node:
                        level.append(node.val)
                        q.append(node.left)
                        q.append(node.right)
                if len(level) > 0:
                    result.append(level)
        
        bfs(root)
        return result
                    



                


        