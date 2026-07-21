class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #we can use BFS to visit neightbors

        islands = 0
        seen = set()


        rows = len(grid)
        columns = len(grid[0])

        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))

            while q:
                directions = [[1,0],[0,1], [-1,0], [0,-1]]
                row,col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if 0 <= r < rows and 0 <= c < columns and grid[r][c] == "1" and (r,c) not in seen:
                        seen.add((r,c))
                        q.append((r,c))

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r,c) not in seen:
                    islands += 1
                    #check its neighbors
                    seen.add((r,c))
                    bfs(r,c)
        

        return islands
        