# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in order traversal DFS
        #go left until you can't go left anymore 
        # THEN go right


        n = 0
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            #gets us all the way to the left

            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            
            cur = cur.right
