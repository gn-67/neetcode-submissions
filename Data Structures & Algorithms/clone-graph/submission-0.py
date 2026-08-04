"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloneMap = {}

        def dfs(node):
            if node in cloneMap:
                return cloneMap[node]
            
            copy = Node(val = node.val)
            cloneMap[node] = copy

            #now we exxpxlore our neighbors
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        
        if node:
            return dfs(node)
        
        return None
        