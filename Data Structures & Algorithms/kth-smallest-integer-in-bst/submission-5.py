# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        #we can use in-order traversal to access the smallest values first
        #then return the kth node in our queue


        #we can use a stack data structure to keep track of our in order traversal

        cur = root
        stack = []
        target = k

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left


            cur = stack.pop()
            target -= 1
            if target == 0:
                return cur.val
            cur = cur.right

        