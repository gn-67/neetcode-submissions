class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #undirected graph
        #we can do a walk adding nodes to a set to track which nodes we've visited
        #we can usea dfs algorithm to traverse each node, makring its connected neighbors as seen
        #if the next node as not been visited, we run dfs on it and increment the count of components


        #first lets create our adjMap

        adjMap = {i : set() for i in range(n)}
        for edge in edges:
            adjMap[edge[0]].add(edge[1])
            adjMap[edge[1]].add(edge[0])
        
        visited = set()
        result = 0



        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for edge in adjMap[node]:
                dfs(edge)
            return

        
        
        for node in range(n):
            if node not in visited:
                result += 1
                dfs(node)
        
        return result




        

        