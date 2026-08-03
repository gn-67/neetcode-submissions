class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #we use bfs to visit our neighbors
        #if we encounter a one, we explore its nieghbors and add the location into seen, that way we know it isn't part of a new island
        #we iterate through each location, checking if its seen or not


        rows = len(grid)
        cols = len(grid[0])

        seen = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))
            seen.add((r,c))

            while q:
                row, col = q.popleft()
                directions = [[1,0], [0,1], [-1,0], [0,-1]]

                for dr, dc in directions:
                    r = row + dr
                    c = col + dc

                    if -1 < r < rows and -1 < c < cols and (r,c) not in seen and grid[r][c] == "1":
                        q.append((r,c))
                        seen.add((r,c))


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in seen :
                    bfs(row, col)
                    islands += 1
 
        
        return islands
        
