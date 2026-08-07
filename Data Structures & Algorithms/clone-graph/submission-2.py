"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #connected, undirected graph
        #^nodes go both ways

        #we are given adjList

        #we can use a hashmap to store the new copy of each node we visit
        #that way when we run DFS we can quickly link our nodes neighbors


        cloneMap = {}


        def dfs(node):
            if node in cloneMap:
                return cloneMap[node]
            
            copy = Node(val = node.val)
            cloneMap[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        
        if not node:
            return None
        
        return dfs(node)



        