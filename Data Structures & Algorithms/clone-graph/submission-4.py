"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:


        #what we want to do use use a hashmap to store the clone nodes
        #that way when we traverse neighbors, if we encounter a node we have already cloned we can pass it back
        #I will traverse this graph with a dfs function

        cloneMap = {}

        def dfs(node):
            if node in cloneMap:
                return cloneMap[node]
            if not node:
                return
            
            copy = Node(val = node.val)
            cloneMap[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        
        return dfs(node)


        