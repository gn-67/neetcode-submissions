class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #a valid tree must be connected and contain no cycles
        #we can use dfs and a set to keep track of which nodes we've visited to ensure that we do not have any cycles in our graph.
        #if we complete a successful walk and the amount of nodes we've visited is the same as the total amount of nodes given, we know we have a valid tree
        #we can also use an adjacency map to map out our edges for each node
        #since the edges are undirected, we need to keep track of a prev node in our function 

        adjMap = {i : set() for i in range(n)}
        for edge in edges:
            adjMap[edge[0]].add(edge[1])
            adjMap[edge[1]].add(edge[0])
        
        visited = set()


        def dfs(node, previous):
            if node in visited:
                return False
            
            visited.add(node)

            for edge in adjMap[node]:
                if edge == previous:
                    continue
                if not dfs(edge, node):
                    return False
                
            return True
        
        if not dfs(0, -1):
            return False
        
        if len(visited) != n:
            return False
        
        return True