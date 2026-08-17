"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:


        #we can use a hashmap to store the clones of nodes
        #we can use that to check if a node has been cloned already
        # we can traverse the graph with dfs

        cloneMap = {}



        def dfs(node):
            if not node:
                return
            if node in cloneMap:
                return cloneMap[node]
            
            clone = Node(val = node.val)
            cloneMap[node] = clone
            #now we have to explore neighbors
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone

        return dfs(node)



        