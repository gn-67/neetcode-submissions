class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # we can use an implementation of dijkstras algorithm here to find the shortest path to end

        #since we are doing dijkstras we can implement this using a minheap
        #and we can have each node processsed store the row, column, and the current highest difference of the path.


        q = [[0,0,0]] #start at 0, 0 with 0 difference  
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        visited = set()


        while q:
            diff, row, col = heapq.heappop(q)
            if (row,col) in visited:
                continue

            visited.add((row,col))

            if row == len(heights) - 1 and col == len(heights[0]) - 1:
                return diff
            
            for dr, dc in directions:
                r = row + dr
                c = col + dc

                if r >= 0 and c >= 0 and r < len(heights) and c < len(heights[0]) and (r,c) not in visited:
                    heapq.heappush(q, [max(abs(heights[r][c] - heights[row][col]), diff),r,c]) 
        

        