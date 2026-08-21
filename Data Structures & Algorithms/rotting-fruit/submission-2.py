class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        rows = len(grid)
        cols = len(grid[0])
        q = collections.deque()
        time = 0
        fresh = 0
        directions = [[0,1],[-1,0],[0,-1], [1,0]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))

        #we are appending ROTTON fruit to the queue
        #so if we add a fruit to the queue, we have to mark it rotten AFTER
        
        while fresh > 0 and q:

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

        if fresh == 0:
            return time
        return -1 

