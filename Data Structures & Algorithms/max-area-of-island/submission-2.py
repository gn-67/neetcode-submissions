class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #similar approach to count islands

        #we when we encounter an island, we use BFS to explore its neighbors and map out the island by adding it to seen
        #we can just keep track of a maxArea and each time we run bfs we keep track of a count, at the end of bfs we return the max between our current maxArea and the islands area
        

        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        maxArea = 0



        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            count = 0
            
            while q:
                row, col = q.popleft()

                count += 1


                directions = [[0,1],[1,0],[-1,0],[0,-1]]

                for dr,dc in directions:
                    r = row + dr
                    c = col + dc
                    if r >= 0 and r < rows and c >=0 and c < cols and grid[r][c] == 1 and (r,c) not in visited:
                        visited.add((r,c))
                        q.append((r,c))

            return count
                

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1 and (r,c) not in visited:
                    maxArea = max(maxArea, bfs(r,c))
        
        return maxArea







    
        