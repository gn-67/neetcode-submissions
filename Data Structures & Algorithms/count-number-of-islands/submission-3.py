class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #we can track which nodes we have visited so that if its a 1 and we visited it already, we know not to tally up our island count
        #we can use backtracking to clean up our walks 
        #we use BFS to explore neighbors cleanly
        #the logic for this problem is that we are only exploring nodes that are "islands", and we map out the entire island by running bfs on a 
        visited = set()
        islands = 0

        rows = len(grid)
        cols = len(grid[0])

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))

            while q:
                row, col = q.popleft()
                directions = [[0,1], [1,0], [-1, 0], [0,-1]]

                for dr, dc in directions:
                    r = row + dr
                    c = col + dc

                    if -1 <= r < rows and -1 <= c < cols and grid[r][c] == "1" and (r,c) not in visited:
                        visited.add((r,c))
                        q.append((r,c))
            
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == "1":
                    islands += 1
                    bfs(r,c)
        
        return islands
            




            



        