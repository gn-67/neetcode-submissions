# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        q = collections.deque()
        q.append(root)


        #while the queue is not empty
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node: #check to make sure node is not null
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                    #wait so when we append root doesn't that append the entire Input: root = [1,2,3,4,5,6,7]??
            if level:
                result.append(level)

        
        return result

