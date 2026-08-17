class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        #we can use bfs to explore each island and map out its size
        #we can use a set to track whcih nodes are a part of an exisitng island

        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))

            while q:
                row, col = q.popleft()
                directions = [[0,1], [1,0], [-1,0], [0,-1]]

                for dr, dc in directions:
                    r = row + dr
                    c = col + dc

                    if r >= 0 and r < rows and c >= 0 and c < cols and (r,c) not in visited and grid[r][c] == "1":
                        visited.add((r,c))
                        q.append((r,c))




        for r in range(rows):
            for c in range(cols):
                if ((r,c)) not in visited and grid[r][c] == "1":
                    islands += 1
                    bfs(r,c)
        
        return islands


        