class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #in this problem we can approach it similarlily to the numebr of islands problem
        #we can keep a global count of components and run dfs on each node,
        #if the node hasn't been visited before, we increase the tally because its part of a new component, all visited nodes will be marked during dfs so any unvisited nodes are new

        visited = set()
        
        adjList = {i : set() for i in range(n)}

        for edge in edges:
            adjList[edge[0]].add(edge[1])
            adjList[edge[1]].add(edge[0])
        
        print(adjList)

        components = 0

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for neighbor in adjList[node]:
                dfs(neighbor)





        for node in range(n):
            if node not in visited:
                components += 1
                dfs(node)
        
        return components
        