class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree = each node has one parent and one child
        #we could probably track that based on node number
        # no cycles -> checking if we visited a node already in a path
        #we should prob map out hte node connections to a data structure
        # a tree must contain all nodes
        
        adjList = {i : set() for i in range(n)}

        for edge in edges:
            if edge[0] in adjList:
                adjList[edge[0]].add(edge[1])
                adjList[edge[1]].add(edge[0])

        print (adjList)
        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            
            
            #need to distinguish "this is my parent"

            
            visited.add(node)
            for child in adjList[node]:
                if child == parent:
                    continue
                if not dfs(child, node):
                    return False
            
            return True
        
        # a tree includes all nodes
        #check each node:
        if not dfs(0, -1):
            return False
        if len(visited) != n:
            return False
        
        return True 



