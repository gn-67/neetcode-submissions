class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows = len(grid)
        cols = len(grid[0])

        seen = set()

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            seen.add((r,c))
            while q:
                r, c = q.popleft()
                directions = [[1,0], [-1, 0], [0,1], [0,-1]]
                for dr, dc in directions: 
                    #how does this iteration work? why not just for i in directions? (four times)
                    row = r + dr
                    col = c + dc
                    if (row,col) not in seen and row < rows and col < cols and row > -1 and col > -1 and grid[row][col] == "1":
                        seen.add((row,col))
                        q.append((row,col))

                



        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1" and (r,c) not in seen:
                    bfs(r,c)
                    islands += 1
                
        return islands