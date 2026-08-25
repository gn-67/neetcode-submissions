class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        #undirected nodes go both ways
        #a tree is valid if its connected and doesn't contain any cycles
        #thus I think we should create a dfs function that checks for cycles
        #I'm using dfs here because in theory we should be able to traverse the entire graph in just one call, and dfs is concise to write and we don't necesarily need to focus on level order traversal here
        #we can use a set to track which nodes we've visited, and after we complete our walk, if the length of our set doesn't equal the amount of nodes given to us in the graph, then we return false since our graph is not connected
        #additionally we can use a prev parameter within our dfs helper function so that we don't explore it since our graph is undirected


        visited = set()
        adjMap = {i : set() for i in range(n)}
        for edge in edges:
            adjMap[edge[0]].add(edge[1])
            adjMap[edge[1]].add(edge[0])

        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)

            for neighbor in adjMap[node]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, node):
                    return False
            
            return True
        
        if not dfs(0, -1):
            return False
        if len(visited) != n:
            return False
        
        return True
        