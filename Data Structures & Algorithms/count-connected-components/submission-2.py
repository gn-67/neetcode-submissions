class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0

        #do i need to use set and track both ways for htis problem?
        adjMap = {i : set() for i in range(n)}
        for edge in edges:
            adjMap[edge[0]].add(edge[1])
            adjMap[edge[1]].add(edge[0])


        seen = set()

        #if its already been seen then we know we've already added it to the count
        # we can use seen to manage nodes that are a part of a collection that have already been visited 


        def dfs(node):
            if node in seen:
                return 
            
        
            seen.add(node)

            for child in adjMap[node]:
                dfs(child)
            
            return





        for i in range(n):

            if i not in seen:
                dfs(i)
                count += 1
            

        return count
