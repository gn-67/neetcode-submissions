class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #since our rot affects neighbors, we can use BFS here
        #we will have to start our BFS search from multiple sources, and increment our time variable each time the rot 'spreads'
        #so to start we have to first mark how many fresh fruit we have and where our rotten fruit are, so we know where to start and stop

        q = collections.deque()
        fresh = 0
        time = 0
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        

        while fresh > 0 and q:
            #in order to grab current snapshot
            for i in range(len(q)):

                row, col = q.popleft()

                for dr, dc in directions:
                    r = row + dr
                    c = col + dc

                    if r >= 0 and r < rows and c >= 0 and c < cols and grid[r][c] == 1:
                        fresh -= 1
                        grid[r][c] = 2
                        q.append((r,c))
                
            time += 1

        if fresh > 0:
            return -1
        
        return time
            



        