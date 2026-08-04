"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #in order to preserve a deep copy we need to make sure each node contains the correct edges to the correct corresponding nodes
        # we can use a hashmap to store copy values and connect copys to their corresponding neighbors

        cloneMap = {}

        #we can use dfs here because we need to explore our neighbors for each node and wire them to the corresponding copys
        def dfs(node):
            if node in cloneMap:
                return cloneMap[node]
            
            copy = Node(val = node.val)
            cloneMap[node] = copy

            #now we explore neighbors
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        

        if node:
            return dfs(node)
        
        else: 
            return None

        