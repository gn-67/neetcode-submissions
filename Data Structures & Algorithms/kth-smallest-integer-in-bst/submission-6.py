# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        

        #we have to use pre order traversal
        #we visit the left most side first because thats where the smallest values lie, then we keep moving back up until we have reached our k smallest element

        cur = root
        stack = []
        result = k

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            result -= 1
            if result == 0:
                return cur.val
            cur = cur.right


