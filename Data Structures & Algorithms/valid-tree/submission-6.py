class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # a tree is a conected graph with no cycles
        # so we should detect cycles or disconectedness then return false
        #we can detect cycles by tracking which nodes we've visited
        # since our tree needs to be connected, we don't need to use backtracking here as in theory eveyrthing should complete in one path, if not then we return false
        #since we are given edges lets change that into an adjList
        #undirected edges = edge goes both ways

        adjList = {i : set() for i in range(n)}
        seen = set()

        for edge in edges:
            adjList[edge[0]].add(edge[1])
            adjList[edge[1]].add(edge[0])

        print(adjList)

        def dfs(node, prev):
            if node in seen:
                return False

            seen.add(node)
            for neighbor in adjList[node]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, node):
                    return False
            #no need to remove node from visited, we do one pass through tallying up our visited nodes
            return True
        
        #if we detect cycle, return false
        if not dfs(0, -1):
            return False
        
        #if the graph is disconeccted, return false

        if len(seen) != n:
            return False
        
        return True
        

        