class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        N = len(grid) 
        if grid[0][0] == 1 or grid[N-1][N-1] == 1:
            return -1  
        q = collections.deque()
        visited = set()
     
        directions = [[0,1], [1,0], [-1,0], [0,-1], [1,1], [-1,-1], [-1,1], [1,-1]]

        q.append((0,0,1))

        while q:
            row, col, length = q.popleft()

            if row == N - 1 and col == N - 1:
                return length

            for dr, dc in directions:
                r = dr + row
                c = dc + col

                if r >= 0 and c >= 0 and r < N and c < N and (r,c) not in visited and grid[r][c] == 0:
                    visited.add((r,c))
                    q.append((r,c,length + 1))
 
        return -1

        