class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #in a grid, breath first search is the most optimal algorithm
        #in our bredth first search, we can queue the current row & column, as well as the current length of path
        #since BFS is most optimal to reach the end, the first path to reach the end is most optimal and we can return that paths length, or return -1 otherwise

        N = len(grid)
        directions = [[0,1], [1,0], [-1,0], [0,-1], [1,1], [-1,-1], [-1,1], [1,-1]]
        visited = set()

        if grid[0][0] == 1 or grid[N-1][N-1] == 1:
            return -1

        q = collections.deque()
        q.append((0,0,1))

        while q:
            row, col, length = q.popleft()

            if row == N - 1 and col == N - 1:
                return length
            
            for dr, dc in directions:
                r = row + dr
                c = col + dc

                if r >= 0 and c >= 0 and c < N and r < N and (r,c) not in visited and grid[r][c] == 0:
                    visited.add((r,c))
                    q.append((r,c,length + 1))
        
        return -1
            


        