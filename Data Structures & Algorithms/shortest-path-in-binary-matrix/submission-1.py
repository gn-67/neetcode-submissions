class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0] == 1 or grid[len(grid) - 1][len(grid) - 1] == 1:
            return -1

        N = len(grid)
        q = collections.deque()
        visited = set()
        directions = [[0,1],[1,0],[-1,0],[0,-1],[1,1], [1,-1], [-1,-1], [-1,1]]

        q.append((0,0,1))

        while q:
            row, column, length = q.popleft()

            if row == N - 1 and column == N - 1:
                return length
            visited.add((row,column))
            #there could be multiple paths to the end
            #first one there is shortest.

            for dr, dc in directions:
                r = row + dr
                c = column + dc
                if r >= 0 and r < N and c >= 0 and c < N and grid[r][c] == 0 and (r,c) not in visited:
                    q.append((r,c,length + 1))
        

        return -1










        
        